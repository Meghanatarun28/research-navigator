from langchain_ollama import (
    ChatOllama,
)

from research_navigator.config.settings import (
    settings,
)


class AnswerGenerator:
    def __init__(self):
        self.model = ChatOllama(
            model=settings.ollama_model,
            temperature=0,
        )

    def generate(
        self,
        query: str,
        results,
    ) -> str:
        if not results:
            return "I do not have enough information in the corpus."

        context_chunks = []

        for result in results[:5]:
            text = result["point"].payload.get(
                "text",
                "",
            )

            section = result["point"].payload.get(
                "section_title",
                "",
            )

            title = result["point"].payload.get(
                "title",
                "",
            )

            context_chunks.append(
                f"""
Title: {title}
Section: {section}

{text[:800]}
"""
            )

        context = "\n\n".join(context_chunks)

        prompt = f"""
You are an expert AI research assistant.

Use ONLY the provided context.

Question:
{query}

Context:
{context}

Instructions:

1. Read all context carefully.
2. Combine information from multiple chunks.
3. Write a complete answer in your own words.
4. Do NOT copy sentences directly.
5. Ignore references, tables, figures, citations and appendix content.
6. Keep the answer between 100 and 200 words.
7. If the answer is not present in the context, say exactly:

"I do not have enough information in the corpus."

Answer:
"""

        try:
            response = self.model.invoke(prompt)

            return response.content.strip()

        except Exception:
            best_chunk = results[0]["point"].payload.get(
                "text",
                "",
            )

            return best_chunk[:500]
