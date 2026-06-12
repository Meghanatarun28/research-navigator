from research_navigator.retrieve.citations import (
    CitationBuilder,
)


class MockPoint:
    def __init__(self):
        self.payload = {
            "doc_id": "paper_1",
            "title": "Test Paper",
            "authors": [
                "John Doe",
                "Jane Doe",
            ],
            "year": 2024,
            "section_title": "INTRODUCTION",
            "source_url": "https://example.com",
        }


def test_build_citations():
    builder = CitationBuilder()

    citations = builder.build([MockPoint()])

    assert len(citations) == 1

    assert citations[0]["title"] == "Test Paper"

    assert citations[0]["year"] == 2024


def test_multiple_authors():
    class MockPoint:
        def __init__(self):
            self.payload = {
                "doc_id": "paper_2",
                "title": "Another Paper",
                "authors": [
                    "Author A",
                    "Author B",
                    "Author C",
                ],
                "year": 2024,
                "section_title": "ABSTRACT",
                "source_url": "https://example.com",
            }

    builder = CitationBuilder()

    citations = builder.build([MockPoint()])

    assert citations[0]["authors"] == "Author A et al."
