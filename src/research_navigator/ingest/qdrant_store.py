from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PayloadSchemaType,
    PointStruct,
    VectorParams,
)


class QdrantStore:
    COLLECTION_NAME = "research_chunks"

    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )

    def create_collection(self):
        collections = self.client.get_collections()

        collection_names = [collection.name for collection in collections.collections]

        if self.COLLECTION_NAME in collection_names:
            print("Collection already exists")

            return

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

        print("Collection created")

    def recreate_collection(self):
        try:
            self.client.delete_collection(
                collection_name=self.COLLECTION_NAME,
            )

            print("Existing collection deleted")

        except Exception:
            pass

        self.create_collection()

        print("Collection recreated")

    def create_payload_indexes(self):
        indexes = [
            (
                "content_type",
                PayloadSchemaType.KEYWORD,
            ),
            (
                "year",
                PayloadSchemaType.INTEGER,
            ),
            (
                "primary_category",
                PayloadSchemaType.KEYWORD,
            ),
            (
                "is_foundational",
                PayloadSchemaType.BOOL,
            ),
            (
                "tags",
                PayloadSchemaType.KEYWORD,
            ),
        ]

        for field_name, schema_type in indexes:
            try:
                self.client.create_payload_index(
                    collection_name=self.COLLECTION_NAME,
                    field_name=field_name,
                    field_schema=schema_type,
                )

            except Exception:
                pass

        print("Payload indexes created")

    def chunk_exists(
        self,
        chunk_id: str,
    ) -> bool:
        try:
            result = self.client.retrieve(
                collection_name=self.COLLECTION_NAME,
                ids=[chunk_id],
            )

            return len(result) > 0

        except Exception:
            return False

    def upsert_chunks(
        self,
        chunks,
        vectors,
        metadata,
    ):
        points = []

        skipped = 0

        for chunk, vector in zip(
            chunks,
            vectors,
        ):
            if self.chunk_exists(chunk.chunk_id):
                skipped += 1

                continue

            payload = {
                # Document metadata
                "doc_id": metadata["doc_id"],
                "content_type": metadata["content_type"],
                "title": metadata["title"],
                "authors": metadata["authors"],
                "year": metadata["year"],
                "month": metadata["month"],
                "primary_category": metadata["primary_category"],
                "secondary_categories": metadata["secondary_categories"],
                "tags": metadata["tags"],
                "is_foundational": metadata["is_foundational"],
                "citation_count": metadata["citation_count"],
                "source_url": metadata["source_url"],
                "local_path": metadata["local_path"],
                # Chunk metadata
                "section_title": chunk.section_title,
                "section_index": chunk.section_index,
                "chunk_index": chunk.chunk_index,
                "content_hash": chunk.content_hash,
                # Content
                "retrievable": chunk.retrievable,
                "text": chunk.text,
            }

            point = PointStruct(
                id=chunk.chunk_id,
                vector=vector,
                payload=payload,
            )

            points.append(point)

        if len(points) > 0:
            self.client.upsert(
                collection_name=self.COLLECTION_NAME,
                points=points,
            )

        print(f"Inserted {len(points)} chunks")

        print(f"Skipped {skipped} existing chunks")

    def collection_stats(self):
        return self.client.get_collection(self.COLLECTION_NAME)
