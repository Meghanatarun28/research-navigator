from research_navigator.retrieve.bm25_retriever import (
    BM25Retriever,
)
from research_navigator.retrieve.retriever import (
    Retriever,
)


class HybridRetriever:
    def __init__(self):
        self.dense = Retriever()

        self.bm25 = BM25Retriever()

    def search(
        self,
        query: str,
        limit: int = 10,
        filters=None,
    ):
        # -------------------------
        # Dense Search
        # -------------------------

        dense_results = self.dense.search(
            query,
            limit=20,
            filters=filters,
        )

        # -------------------------
        # BM25 Search
        # -------------------------

        bm25_results = self.bm25.search(
            query,
            limit=20,
        )

        fused = {}

        # -------------------------
        # Dense Contribution (70%)
        # -------------------------

        for point in dense_results:
            chunk_id = str(point.id)

            fused[chunk_id] = {
                "point": point,
                "score": point.score * 0.7,
            }

        # -------------------------
        # BM25 Contribution (30%)
        # -------------------------

        max_bm25 = max(
            [score for _, score in bm25_results],
            default=1.0,
        )

        for point, score in bm25_results:
            chunk_id = str(point.id)

            normalized_score = score / max_bm25

            if chunk_id in fused:
                fused[chunk_id]["score"] += normalized_score * 0.3

            else:
                fused[chunk_id] = {
                    "point": point,
                    "score": normalized_score * 0.3,
                }

        # -------------------------
        # Section Boosting
        # -------------------------

        important_sections = [
            "ABSTRACT",
            "INTRODUCTION",
            "OVERVIEW",
            "BACKGROUND",
            "CONCLUSION",
        ]

        bad_sections = [
            "REFERENCES",
            "ACKNOWLEDGMENTS",
            "APPENDIX",
            "BIBLIOGRAPHY",
        ]

        for item in fused.values():
            section = (
                item["point"]
                .payload.get(
                    "section_title",
                    "",
                )
                .upper()
            )

            if section in important_sections:
                item["score"] += 0.40

            elif section in bad_sections:
                item["score"] -= 0.50

        # -------------------------
        # Remove Low Quality Chunks
        # -------------------------

        filtered = []

        for item in fused.values():
            text = (
                item["point"]
                .payload.get(
                    "text",
                    "",
                )
                .lower()
            )

            if (
                "references" in text[:100]
                or "bibliography" in text[:100]
                or "acknowledgment" in text[:100]
            ):
                continue

            filtered.append(item)

        # -------------------------
        # Final Ranking
        # -------------------------

        ranked = sorted(
            filtered,
            key=lambda x: x["score"],
            reverse=True,
        )

        return ranked[:limit]
