from dataclasses import dataclass
from pathlib import Path
from typing import List

import fitz


@dataclass
class ParsedSection:
    title: str
    content: str
    section_index: int


@dataclass
class ParsedDocument:
    doc_id: str
    title: str
    sections: List[ParsedSection]


class PDFParser:
    def parse(
        self,
        pdf_path: str,
        doc_id: str,
    ) -> ParsedDocument:
        document = fitz.open(pdf_path)

        full_text = ""

        for page in document:
            full_text += page.get_text("text")
            full_text += "\n"

        sections = self._extract_sections(full_text)

        return ParsedDocument(
            doc_id=doc_id,
            title=(sections[0].title if sections else doc_id),
            sections=sections,
        )

    def _extract_sections(
        self,
        text: str,
    ) -> List[ParsedSection]:
        sections: List[ParsedSection] = []

        current_title = "UNKNOWN"

        # FIX 1
        current_lines: List[str] = []

        section_index = 0

        for line in text.splitlines():
            line = line.strip()

            if not line:
                continue

            if len(line) < 100 and line.isupper():
                if current_lines:
                    sections.append(
                        ParsedSection(
                            title=current_title,
                            content="\n".join(current_lines),
                            section_index=section_index,
                        )
                    )

                    section_index += 1

                current_title = line

                current_lines = []

            else:
                current_lines.append(line)

        if current_lines:
            sections.append(
                ParsedSection(
                    title=current_title,
                    content="\n".join(current_lines),
                    section_index=section_index,
                )
            )

        return sections


class MarkdownParser:
    def parse(
        self,
        md_path: str,
        doc_id: str,
    ) -> ParsedDocument:
        text = Path(md_path).read_text(encoding="utf-8")

        sections: List[ParsedSection] = []

        current_title = "ROOT"

        # FIX 2
        current_lines: List[str] = []

        section_index = 0

        for line in text.splitlines():
            if line.startswith("#"):
                if current_lines:
                    sections.append(
                        ParsedSection(
                            title=current_title,
                            content="\n".join(current_lines),
                            section_index=section_index,
                        )
                    )

                    section_index += 1

                current_title = line.lstrip("#").strip()

                current_lines = []

            else:
                current_lines.append(line)

        if current_lines:
            sections.append(
                ParsedSection(
                    title=current_title,
                    content="\n".join(current_lines),
                    section_index=section_index,
                )
            )

        return ParsedDocument(
            doc_id=doc_id,
            title=(sections[0].title if sections else doc_id),
            sections=sections,
        )
