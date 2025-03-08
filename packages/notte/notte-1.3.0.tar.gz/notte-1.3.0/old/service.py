from calendar import c
import logging
from importlib import resources

from playwright.async_api import Page

from notte.pipe.preprocessing.dom.types import (
	DOMBaseNode,
	DOMElementNode,
	DOMState,
	DOMTextNode,
	SelectorMap,
)
from notte.browser.dom_tree import DomNode as NotteDomNode
from notte.pipe.preprocessing.a11y.id_generation import generate_sequential_ids, simple_generate_sequential_ids
from notte.pipe.preprocessing.a11y.notte_selector import generate_notte_selector

logger = logging.getLogger(__name__)


class DomService:
	def __init__(self, page: Page):
		self.page: Page = page
		self.xpath_cache: dict[str, str] = {}

	# region - Clickable elements
	async def get_clickable_elements(
		self,
		highlight_elements: bool = True,
		focus_element: int = -1,
		viewport_expansion: int = 0,
	) -> DOMState:
		element_tree = await self._build_dom_tree(highlight_elements, focus_element, viewport_expansion)
		selector_map = self._create_selector_map(element_tree)

		return DOMState(element_tree=element_tree, selector_map=selector_map)

	async def _build_dom_tree(
		self,
		highlight_elements: bool = True,
		focus_element: int = -1,
		viewport_expansion: int = 0,
	) -> DOMElementNode:
		js_code = resources.read_text('notte.browser.dom', 'buildDomNode.js')

		args = {
			'doHighlightElements': highlight_elements,
			'focusHighlightIndex': focus_element,
			'viewportExpansion': viewport_expansion,
		}

		eval_page = await self.page.evaluate(js_code, args)  # This is quite big, so be careful
		html_to_dict = self._parse_node(eval_page)

		if html_to_dict is None or not isinstance(html_to_dict, DOMElementNode):
			raise ValueError('Failed to parse HTML to dictionary')

		return html_to_dict

	async def build_dom_tree(self) -> NotteDomNode:
		dom_tree = await self._build_dom_tree()
		for step in [simple_generate_sequential_ids, generate_notte_selector]:
			dom_tree = step(dom_tree)
			if isinstance(dom_tree, dict):
				raise ValueError(f"Dom tree is not a valid NotteDomNode: {dom_tree}")
		return dom_tree.to_notte_domnode()

	def _create_selector_map(self, element_tree: DOMElementNode) -> SelectorMap:
		selector_map = {}

		def process_node(node: DOMBaseNode):
			if isinstance(node, DOMElementNode):
				if node.highlight_index is not None:
					selector_map[node.highlight_index] = node

				for child in node.children:
					process_node(child)

		process_node(element_tree)
		return selector_map

	def _parse_node(
		self,
		node_data: dict[str, str | int | list[str] | dict[str, str] | bool | None],
		parent: 'DOMElementNode | None' = None,
	) -> 'DOMBaseNode | None':
		if not node_data:
			return None

		if node_data.get('type') == 'TEXT_NODE':
			text_node = DOMTextNode(
				text=node_data['text'],
				is_visible=node_data['isVisible'],
				parent=parent,
			)

			return text_node

		tag_name = node_data['tagName']

		element_node = DOMElementNode(
			tag_name=tag_name,
			xpath=node_data['xpath'],
			attributes=node_data.get('attributes', {}),
			is_visible=node_data.get('isVisible', False),
			is_interactive=node_data.get('isInteractive', False),
			is_top_element=node_data.get('isTopElement', False),
			highlight_index=node_data.get('highlightIndex'),
			shadow_root=node_data.get('shadowRoot', False),
			parent=parent,
		)

		children: list[DOMBaseNode] = []
		for child in node_data.get('children', []):
			if child is not None:
				child_node = self._parse_node(child, parent=element_node)
				if child_node is not None:
					children.append(child_node)

		element_node.children = children

		return element_node

	# endregion