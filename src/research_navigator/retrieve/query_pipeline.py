from research_navigator.retrieve.answer_generator import (
    AnswerGenerator,
)
from research_navigator.retrieve.citations import (
    CitationBuilder,
)
from research_navigator.retrieve.hybrid_retriever import (
    HybridRetriever,
)
from research_navigator.retrieve.query_understanding import (
    QueryUnderstanding,
)


class QueryPipeline:
    MIN_SCORE = 0.40

    def __init__(self):
        self.retriever = HybridRetriever()

        self.query_understanding = QueryUnderstanding()

        self.citation_builder = CitationBuilder()

        self.answer_generator = AnswerGenerator()

    def answer(
        self,
        query: str,
    ):
        filters = self.query_understanding.extract_filters(query)

        results = self.retriever.search(
            query,
            filters=filters,
        )

        if not results:
            return (
                "I don't have enough relevant "
                "material in the corpus to "
                "answer this confidently."
            )

        best_score = results[0]["score"]

        if best_score < self.MIN_SCORE:
            return (
                "I don't have enough relevant "
                "material in the corpus to "
                "answer this confidently."
            )

        preferred_sections = [
            "ABSTRACT",
            "INTRODUCTION",
            "OVERVIEW",
            "BACKGROUND",
        ]

        results = sorted(
            results,
            key=lambda x: (
                x["point"]
                .payload.get(
                    "section_title",
                    "",
                )
                .upper()
                not in preferred_sections
            ),
        )

        citation_points = [result["point"] for result in results]

        citations = self.citation_builder.build(citation_points)

        generated_answer = self.answer_generator.generate(
            query,
            results,
        )

        answer = []

        answer.append(generated_answer)

        answer.append("\n\nReferences:\n")

        for citation in citations:
            answer.append(
                f"[{citation['number']}] "
                f"{citation['title']} | "
                f"{citation['authors']} | "
                f"{citation['year']} | "
                f"{citation['section']} | "
                f"{citation['url']}"
            )

        return "\n".join(answer)
