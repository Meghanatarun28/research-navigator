from pathlib import Path

from research_navigator.ingest.manifest_loader import (
    ManifestLoader,
)
from research_navigator.ingest.pipeline import (
    IngestionPipeline,
)
from research_navigator.ingest.qdrant_store import (
    QdrantStore,
)

MANIFEST_PATH = (
    r"..\ai-research-navigator-corpus"
    r"\ai-research-navigator-corpus"
    r"\manifest.json"
)

CORPUS_ROOT = (
    r"..\ai-research-navigator-corpus"
    r"\ai-research-navigator-corpus"
)


def ingest():
    pipeline = IngestionPipeline(
        manifest_path=MANIFEST_PATH,
        corpus_root=CORPUS_ROOT,
    )

    pipeline.ingest_corpus()


def validate():
    print("\n=== Validation ===")

    try:
        loader = ManifestLoader(MANIFEST_PATH)

        documents = loader.manifest["documents"]

        total_docs = len(documents)

        missing_files = []

        corpus_root = Path(CORPUS_ROOT)

        for document in documents:
            file_path = corpus_root / document["local_path"]

            if not file_path.exists():
                missing_files.append(str(file_path))

        print(f"Manifest documents: {total_docs}")

        print(f"Files found: {total_docs - len(missing_files)}")

        print(f"Missing files: {len(missing_files)}")

        store = QdrantStore()

        info = store.collection_stats()

        print(f"Collection: {store.COLLECTION_NAME}")

        print(f"Points: {info.points_count}")

        print("\nValidation successful")

    except Exception as e:
        print(f"Validation failed: {e}")


def stats():
    print("\n=== Collection Stats ===")

    try:
        store = QdrantStore()

        info = store.collection_stats()

        print(f"Collection: {store.COLLECTION_NAME}")

        print(f"Points: {info.points_count}")

        print(f"Status: {info.status}")

        loader = ManifestLoader(MANIFEST_PATH)

        documents = loader.manifest["documents"]

        content_types = {}

        years = {}

        for document in documents:
            content_type = document["content_type"]

            year = document["year"]

            content_types[content_type] = (
                content_types.get(
                    content_type,
                    0,
                )
                + 1
            )

            years[year] = (
                years.get(
                    year,
                    0,
                )
                + 1
            )

        print("\nBy Content Type:")

        for key, value in sorted(content_types.items()):
            print(f"  {key}: {value}")

        print("\nBy Year:")

        for key, value in sorted(years.items()):
            print(f"  {key}: {value}")

    except Exception as e:
        print(f"Failed to fetch stats: {e}")


def reindex():
    store = QdrantStore()

    store.create_payload_indexes()

    print("Reindex complete")
