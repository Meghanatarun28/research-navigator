class CitationBuilder:
    def build(
        self,
        results,
    ):
        citations = []

        seen_docs = set()

        counter = 1

        for point in results:
            payload = point.payload

            doc_id = payload["doc_id"]

            if doc_id in seen_docs:
                continue

            seen_docs.add(doc_id)

            authors = payload.get(
                "authors",
                [],
            )

            if len(authors) >= 3:
                author_text = f"{authors[0]} et al."

            else:
                author_text = ", ".join(authors)

            citation = {
                "number": counter,
                "doc_id": doc_id,
                "title": payload["title"],
                "authors": author_text,
                "year": payload["year"],
                "section": payload["section_title"],
                "url": payload["source_url"],
            }

            citations.append(citation)

            counter += 1

        return citations
