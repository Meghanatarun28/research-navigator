from dataclasses import dataclass
from pathlib import Path


@dataclass
class ParsedDocument:
    doc_id: str
    text: str


class MarkdownParser:
    def parse(
        self,
        markdown_path: str,
        doc_id: str,
    ):
        text = Path(markdown_path).read_text(encoding="utf-8")

        return ParsedDocument(
            doc_id=doc_id,
            text=text,
        )
