import uuid
from dataclasses import dataclass
from hashlib import sha256

from research_navigator.ingest.parser import (
    ParsedDocument,
)


@dataclass
class Chunk:
    chunk_id: str
    chunk_index: int
    section_title: str
    section_index: int
    text: str
    content_hash: str
    retrievable: bool


class Chunker:
    SKIP_SECTIONS = [
        "references",
        "bibliography",
        "appendix",
        "acknowledgements",
        "acknowledgments",
    ]

    def __init__(
        self,
        chunk_size: int = 1000,
    ):
        self.chunk_size = chunk_size

    def chunk_document(
        self,
        document: ParsedDocument,
    ) -> list[Chunk]:
        chunks = []

        chunk_index = 0

        for section in document.sections:
            section_title = (section.title or "").strip()

            if section_title.lower() in self.SKIP_SECTIONS:
                print(f"Skipping section: {section_title}")

                continue

            retrievable = True

            text = section.content

            start = 0

            while start < len(text):
                end = start + self.chunk_size

                chunk_text = text[start:end]

                content_hash = sha256(chunk_text.encode("utf-8")).hexdigest()

                chunk_id = str(
                    uuid.uuid5(
                        uuid.NAMESPACE_DNS,
                        (f"{document.doc_id}_{chunk_index}_{content_hash}"),
                    )
                )

                chunks.append(
                    Chunk(
                        chunk_id=chunk_id,
                        chunk_index=chunk_index,
                        section_title=section_title,
                        section_index=section.section_index,
                        text=chunk_text,
                        content_hash=content_hash,
                        retrievable=retrievable,
                    )
                )

                chunk_index += 1

                start = end

        return chunks
