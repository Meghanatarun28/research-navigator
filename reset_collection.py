from research_navigator.ingest.qdrant_store import (
    QdrantStore,
)

store = QdrantStore()

store.recreate_collection()

store.create_payload_indexes()

print("Collection reset complete")
