from dataclasses import field, dataclass
from functools import cached_property
from typing import TYPE_CHECKING
from typing_extensions import override
from notte.browser.dom.history_tree_processor.views import HashedDomElement
from notte.browser.dom_tree import NodeSelectors
from notte.browser.dom_tree import DomAttributes, ComputedDomAttributes, DomNode as NotteDomNode
from notte.browser.node_type import NodeRole, NodeType
from loguru import logger
# Avoid circular import issues
if TYPE_CHECKING:
    from .views import DOMElementNode
    
    
VERBOSE = False


@dataclass(frozen=False)
class DOMBaseNode:
    is_visible: bool
    highlight_index:int | None
    parent: 'DOMElementNode | None'
    notte_id: str | None = field(init=False, default=None)
    notte_selector: str | None = field(init=False, default=None)
    children: list['DOMBaseNode'] = field(init=False, default_factory=list)
    # Use None as default and set parent later to avoid circular reference issues

    def __post_init__(self) -> None:
        self.children = []
        self.notte_selector = None
        self.notte_id = None
 
    def to_dict(self) -> dict[str, str]:
        raise NotImplementedError('to_dict method not implemented for DOMBaseNode')

    def to_notte_domnode(self) -> NotteDomNode:
        raise NotImplementedError('to_notte_domnode method not implemented for DOMBaseNode')
    
    @property
    def name(self) -> str:
        raise NotImplementedError('name property not implemented for DOMBaseNode')
    
    @property
    def role(self) -> str:
        raise NotImplementedError('role property not implemented for DOMBaseNode')


@dataclass(frozen=False)
class DOMTextNode(DOMBaseNode):
    text: str
    type: str = 'TEXT_NODE'
    highlight_index:int | None = None

    def has_parent_with_highlight_index(self) -> bool:
        current = self.parent
        while current is not None:
            if current.highlight_index is not None:
                return True
            current = current.parent
        return False

    @override
    def to_dict(self) -> dict[str, str]:
        return {
            'role': 'text',
            'text': self.text,
        }
        
    @property
    @override
    def role(self) -> str:
        return 'text'
    
    @property
    @override
    def name(self) -> str:
        return self.text
    
    @override
    def to_notte_domnode(self) -> NotteDomNode:
        return NotteDomNode(
            id=self.notte_id,
            role=NodeRole.from_value(self.role),
            type=NodeType.TEXT,
            text=self.name,
            children=[],
            computed_attributes=ComputedDomAttributes(
                in_viewport=self.is_visible,
            ),
            
        )


@dataclass(frozen=False)
class DOMElementNode(DOMBaseNode):
    """
    xpath: the xpath of the element from the last root node (shadow root or iframe OR document if no shadow root or iframe).
    To properly reference the element we need to recursively switch the root node until we find the element (work you way up the tree with `.parent`)
    """

    tag_name: str
    xpath: str
    attributes: dict[str, str]
    is_interactive: bool = False
    is_top_element: bool = False
    shadow_root: bool = False

    def __repr__(self) -> str:
        tag_str = f'<{self.tag_name}'

        # Add attributes
        for key, value in self.attributes.items():
            tag_str += f' {key}="{value}"'
        tag_str += '>'

        # Add extra info
        extras:list[str] = []
        if self.is_interactive:
            extras.append('interactive')
        if self.is_top_element:
            extras.append('top')
        if self.shadow_root:
            extras.append('shadow-root')
        if self.highlight_index is not None:
            extras.append(f'highlight:{self.highlight_index}')

        if extras:
            tag_str += f' [{", ".join(extras)}]'

        return tag_str

    @cached_property
    def hash(self) -> HashedDomElement:
        from notte.browser.dom.history_tree_processor.service import (
            HistoryTreeProcessor,
        )

        return HistoryTreeProcessor._hash_dom_element(self)

    def get_all_text_till_next_clickable_element(self, max_depth: int = -1) -> str:
        text_parts: list[str] = []

        def collect_text(node: DOMBaseNode, current_depth: int) -> None:
            if max_depth != -1 and current_depth > max_depth:
                return

            # Skip this branch if we hit a highlighted element (except for the current node)
            if (
                isinstance(node, DOMElementNode)
                and node != self
                and node.highlight_index is not None
            ):
                return

            if isinstance(node, DOMTextNode):
                text_parts.append(node.text)
            elif isinstance(node, DOMElementNode):
                for child in node.children:
                    collect_text(child, current_depth + 1)

        collect_text(self, 0)
        return '\n'.join(text_parts).strip()

    def clickable_elements_to_string(self, include_attributes: list[str] = []) -> str:
        """Convert the processed DOM content to HTML."""
        formatted_text: list[str] = []

        def process_node(node: DOMBaseNode, depth: int) -> None:
            if isinstance(node, DOMElementNode):
                # Add element with highlight_index
                if node.highlight_index is not None:
                    attributes_str = ''
                    if include_attributes:
                        attributes_str = ' ' + ' '.join(
                            f'{key}="{value}"'
                            for key, value in node.attributes.items()
                            if key in include_attributes
                        )
                    formatted_text.append(
                        f'{node.highlight_index}[:]<{node.tag_name}{attributes_str}>{node.get_all_text_till_next_clickable_element()}</{node.tag_name}>'
                    )

                # Process children regardless
                for child in node.children:
                    process_node(child, depth + 1)

            elif isinstance(node, DOMTextNode):
                # Add text only if it doesn't have a highlighted parent
                if not node.has_parent_with_highlight_index():
                    formatted_text.append(f'_[:]{node.text}')

        process_node(self, 0)
        return '\n'.join(formatted_text)

    def get_file_upload_element(self, check_siblings: bool = True) -> 'DOMElementNode | None':
        # Check if current element is a file input
        if self.tag_name == 'input' and self.attributes.get('type') == 'file':
            return self

        # Check children
        for child in self.children:
            if isinstance(child, DOMElementNode):
                result = child.get_file_upload_element(check_siblings=False)
                if result:
                    return result

        # Check siblings only for the initial call
        if check_siblings and self.parent:
            for sibling in self.parent.children:
                if sibling is not self and isinstance(sibling, DOMElementNode):
                    result = sibling.get_file_upload_element(check_siblings=False)
                    if result:
                        return result

        return None
    
    @property
    @override
    def role(self) -> str:
        # transform to axt role
        if self.attributes.get('role'):
            return self.attributes.get('role')
        if self.tag_name is None:
            if len(self.attributes) == 0 and len(self.children) == 0:
                return 'none'
            raise ValueError(f'No tag_name found for element: {self} with attributes: {self.attributes}')
        clean_tag_name = self.tag_name.lower().replace('-', '').replace('_', '')
        match self.tag_name.lower():
            # Structural elements
            case 'body':
                return 'WebArea'
            case 'nav':
                return 'navigation'
            case 'main':
                return 'main'
            case 'header':
                return 'banner'
            case 'footer':
                return 'contentinfo'
            case 'aside':
                return 'complementary'
            case 'section' | 'article':
                return 'article'
            case 'div':
                return 'group'
            
            # Interactive elements
            case 'a':
                return 'link'
            case 'button':
                return 'button'
            case 'input':
                input_type = self.attributes.get('type', 'text').lower()
                match input_type:
                    # TODO: could create a special type for submit/reset
                    case 'button' | 'submit' | 'reset':
                        return 'button'
                    case 'radio':
                        return 'radio'
                    case 'checkbox':
                        return 'checkbox'
                    case 'search':
                        return 'searchbox'
                    case _:
                        return 'textbox'
            case 'select':
                return 'combobox'
            case 'textarea':
                return 'textbox'
            case 'option':
                return 'option'
            
            # Text elements
            case 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6':
                return 'heading'
            case 'p':
                return 'paragraph'
            case 'span' | 'strong' | 'em' | 'small' | 'bdi' | 'i':
                return 'text'
            case 'label':
                return 'LabelText'
            case 'blockquote':
                return 'blockquote'
            case 'code' | 'pre':
                return 'code'
            case 'time':
                return 'time'
            case 'br':
                return 'LineBreak'
            
            # List elements
            case 'ul' | 'ol' | 'dl':
                return 'list'
            case 'li':
                return 'listitem'
            case 'dt' | 'dd':
                return 'listitem'
            
            # Table elements
            case 'table':
                return 'table'
            case 'tr':
                return 'row'
            case 'td':
                return 'cell'
            case 'th':
                return 'columnheader'
            case 'thead' | 'tbody' | 'tfoot':
                return 'rowgroup'
            
            # Media elements
            case 'img':
                return 'img'
            case 'figure':
                return 'figure'
            case 'iframe':
                return 'Iframe'
            
            # Form elements
            case 'form':
                return 'form'
            case 'fieldset':
                return 'group'
            case 'dialog':
                return 'dialog'
            case 'progress':
                return 'progressbar'
            case 'meter':
                return 'meter'
            
            # Menu elements
            case 'menu':
                return 'menu'
            case 'menuitem':
                return 'menuitem'
            
            # Default case
            case 'hr':
                return 'separator'
            case _:
                roles_to_check= [
                    'menuitemcheckbox',
                    'menuitemradio',
                    'menuitem',
                    "menu",
                    "dialog"
                ]
                for role in roles_to_check:
                    if role in clean_tag_name:
                        return role
                if 'popup' in clean_tag_name:
                    return 'MenuListPopup'
                
                if VERBOSE:
                    logger.warning(f'No role found for tag: {self.tag_name} with attributes: {self.attributes}')
                return 'generic'

    @property
    @override
    def name(self) -> str:
        if len(self.attributes) == 0:
            return ''
        # Check explicit ARIA labeling
        if 'aria-label' in self.attributes:
            return self.attributes.get('aria-label')
        
        # Check aria-labelledby if present
        if 'aria-labelledby' in self.attributes:
            # Note: This would require access to other elements
            # TODO: Implement aria-labelledby resolution
            pass
        
        # Check for standard labeling attributes
        for attr in ['name', 'title', 'alt', 'placeholder', 'value']:
            if attr in self.attributes:
                value = self.attributes.get(attr)
                if value and value.strip():
                    return value.strip()
        
        # Check for button/input value
        if self.tag_name.lower() in ['button', 'input']:
            if 'value' in self.attributes:
                value = self.attributes.get('value')
                if value and value.strip():
                    return value.strip()
        
        # Check for text content for certain elements
        if self.tag_name.lower() in ['button', 'a', 'label']:
            text_content = self._get_text_content()
            if text_content and text_content.strip():
                return text_content.strip()
            
        if self.tag_name.lower() in ['img', 'a']:
            if 'src' in self.attributes:
                return self.attributes['src']
            if 'href' in self.attributes:
                return self.attributes['href']
            
        if self.tag_name.lower() in [
            'body', 'main', 'div', 'section', 'article', 'header', 'footer', 'aside',
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'span', 'label', 'strong', 'em', 'small',
            'bdi', 'li', 'ol', 'ul', 'dl', 'dt', 'dd',
            'table', 'tr', 'td', 'th', 'thead', 'tbody', 'tfoot',
            'img', 'figure', 'iframe',
            'form', 'fieldset',
            'dialog', 'progress',
            'meter',
            'menu', 'menuitem', 
            'hr', 'br','p','i'
        ]:
            # TODO: create a better name computation using text children and attributes
            return ''
        
        if self.tag_name.lower() in ['footer']:
            return self.tag_name
        
        if self.tag_name.lower() in ['button']:
            return self.attributes.get('type') or ""
        
        first_5_attrs = list(self.attributes.items())[:5]
        if VERBOSE:
            logger.error(f'No name found for element: {self} with attributes: {first_5_attrs}')
        return ''

    def _get_text_content(self) -> str:
        """Recursively get text content from child text nodes."""
        def extract_text(node: DOMBaseNode) -> str:
            if isinstance(node, DOMTextNode):
                return node.text if node.is_visible else ""
            elif isinstance(node, DOMElementNode):
                return "".join(extract_text(child) for child in node.children)
            return ""
        
        return extract_text(self)

    def to_dict(self) -> dict[str, str]:
        role, name = self.role, self.name
        if (name == "" or role == "") and len(self.children) == 0:
            return {}
        base =  {
            'role': role,
            'name': name
        } 
        if self.children:
            base['children'] = [child.to_dict() for child in self.children]
        return base

    @override
    def to_notte_domnode(self) -> NotteDomNode:
        
        return NotteDomNode(
            id=self.notte_id,
            type=NodeType.INTERACTION if self.is_interactive else NodeType.OTHER,
            role=NodeRole.from_value(self.role),
            text=self.name,
            children=[child.to_notte_domnode() for child in self.children],
            attributes=DomAttributes.init(
                tag_name=self.tag_name,
                **self.attributes
            ),
            computed_attributes=ComputedDomAttributes(
                in_viewport=self.is_visible,
                is_interactive=self.is_interactive,
                is_top_element=self.is_top_element,
                shadow_root=self.shadow_root,
                highlight_index=self.highlight_index,
                selectors=NodeSelectors(
                    xpath_selector=self.xpath,
                    notte_selector=self.notte_selector
                ),
            ),
        )

    
class ElementTreeSerializer:
    @staticmethod
    def serialize_clickable_elements(element_tree: DOMElementNode) -> str:
        return element_tree.clickable_elements_to_string()

    @staticmethod
    def dom_element_node_to_json(element_tree: DOMElementNode) -> dict[str, str | int | list[str] | dict[str, str] | bool | None]:
        def node_to_dict(node: DOMBaseNode) -> dict[str, str | int | list[str] | dict[str, str] | bool | None]:
            if isinstance(node, DOMTextNode):
                return {'type': 'text', 'text': node.text}
            ##elif isinstance(node, DOMElementNode):
            return {
                'type': 'element',
                'tag_name': node.tag_name,
                'attributes': node.attributes,
                'highlight_index': node.highlight_index,
                'children': [node_to_dict(child) for child in node.children],
            }
            #return {}

        return node_to_dict(element_tree)


SelectorMap = dict[int, DOMElementNode]


@dataclass
class DOMState:
    element_tree: DOMElementNode
    selector_map: SelectorMap