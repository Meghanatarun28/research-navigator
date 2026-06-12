from qdrant_client import QdrantClient
from rank_bm25 import BM25Okapi


class BM25Retriever:
    COLLECTION_NAME = "research_chunks"

    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )

        self.documents = []

        self.points = []

        self._load_documents()

    def _load_documents(self):
        offset = None

        while True:
            points, offset = self.client.scroll(
                collection_name=self.COLLECTION_NAME,
                limit=1000,
                offset=offset,
                with_payload=True,
            )

            self.points.extend(points)

            if offset is None:
                break

        self.documents = [point.payload["text"] for point in self.points]

        tokenized_docs = [doc.lower().split() for doc in self.documents]

        self.bm25 = BM25Okapi(tokenized_docs)

        print(f"Loaded {len(self.documents)} chunks")

    def search(
        self,
        query: str,
        limit: int = 5,
    ):
        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(
                self.points,
                scores,
            ),
            key=lambda x: x[1],
            reverse=True,
        )

        return ranked[:limit]
