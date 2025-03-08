from dataclasses import dataclass

@dataclass
class HashedDomElement:
	"""
	Hash of the dom element to be used as a unique identifier
	"""

	branch_path_hash: str
	attributes_hash: str
	# text_hash: str


@dataclass
class DOMHistoryElement:
	tag_name: str
	xpath: str
	highlight_index: int | None
	entire_parent_branch_path: list[str]
	attributes: dict[str, str]
	shadow_root: bool = False

	def to_dict(self) -> dict[str, str | int | list[str] | dict[str, str] | bool | None]:
		return {
			'tag_name': self.tag_name,
			'xpath': self.xpath,
			'highlight_index': self.highlight_index,
			'entire_parent_branch_path': self.entire_parent_branch_path,
			'attributes': self.attributes,
			'shadow_root': self.shadow_root,
		}