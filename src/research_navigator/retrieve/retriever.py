from typing import Any

from qdrant_client import (
    QdrantClient,
)
from qdrant_client.models import (
    FieldCondition,
    Filter,
    MatchValue,
    Range,
)
from sentence_transformers import (
    SentenceTransformer,
)


class Retriever:
    COLLECTION_NAME = "research_chunks"

    def __init__(
        self,
    ) -> None:
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )

        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def build_filter(
        self,
        filters: dict,
    ) -> Filter | None:
        conditions: list[Any] = []

        if "year_gte" in filters:
            conditions.append(
                FieldCondition(
                    key="year",
                    range=Range(gte=filters["year_gte"]),
                )
            )

        if "tags" in filters:
            for tag in filters["tags"]:
                conditions.append(
                    FieldCondition(
                        key="tags",
                        match=MatchValue(value=tag),
                    )
                )

        if not conditions:
            return None

        return Filter(must=conditions)

    def search(
        self,
        query: str,
        limit: int = 5,
        filters: dict | None = None,
    ):
        query_vector = self.model.encode(
            query,
            normalize_embeddings=True,
        ).tolist()

        qdrant_filter = self.build_filter(filters or {})

        results = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=query_vector,
            query_filter=qdrant_filter,
            limit=limit,
        )

        return results.points

    def pretty_print(
        self,
        results,
    ) -> None:
        print(f"\nResults found: {len(results)}")

        for index, point in enumerate(
            results,
            start=1,
        ):
            print("\n" + "=" * 80)

            print(f"Rank: {index}")

            print(f"Score: {point.score:.4f}")

            print(f"Title: {point.payload.get('title')}")

            print(f"Section: {point.payload.get('section_title')}")

            print(f"Year: {point.payload.get('year')}")

            print(f"Tags: {point.payload.get('tags')}")

            text = point.payload.get(
                "text",
                "",
            )

            print(f"Text:\n{text[:500]}")
