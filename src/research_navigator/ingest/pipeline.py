from pathlib import Path

from research_navigator.ingest.chunker import Chunker
from research_navigator.ingest.embedder import Embedder
from research_navigator.ingest.manifest_loader import ManifestLoader
from research_navigator.ingest.markdown_parser import MarkdownParser
from research_navigator.ingest.parser import PDFParser
from research_navigator.ingest.qdrant_store import QdrantStore


class IngestionPipeline:
    def __init__(
        self,
        manifest_path: str,
        corpus_root: str,
    ):
        self.manifest_loader = ManifestLoader(manifest_path)

        self.corpus_root = Path(corpus_root)

        self.pdf_parser = PDFParser()

        self.markdown_parser = MarkdownParser()

        self.chunker = Chunker()

        self.embedder = Embedder()

        self.store = QdrantStore()

    def ingest_document(
        self,
        metadata: dict,
    ):
        doc_id = metadata["doc_id"]

        local_path = self.corpus_root / metadata["local_path"]

        if not local_path.exists():
            print(f"Missing file: {local_path}")

            return

        print(f"Ingesting: {doc_id}")

        if local_path.suffix.lower() == ".pdf":
            document = self.pdf_parser.parse(
                str(local_path),
                doc_id,
            )

        elif local_path.suffix.lower() == ".md":
            document = self.markdown_parser.parse(
                str(local_path),
                doc_id,
            )

        else:
            print(f"Unsupported file type: {local_path}")

            return

        chunks = self.chunker.chunk_document(document)

        vectors = self.embedder.embed_batch([chunk.text for chunk in chunks])

        self.store.upsert_chunks(
            chunks,
            vectors,
            metadata,
        )

    def ingest_corpus(self):
        self.store.create_collection()

        documents = self.manifest_loader.manifest["documents"]

        total_docs = len(documents)

        print(f"Found {total_docs} documents")

        for metadata in documents:
            try:
                self.ingest_document(metadata)

            except Exception as e:
                print(f"Failed: {metadata['doc_id']}")

                print(e)

        print("\nCorpus ingestion completed")
