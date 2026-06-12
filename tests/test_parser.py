from research_navigator.ingest.parser import (
    MarkdownParser,
    PDFParser,
)


def test_markdown_parser():
    parser = MarkdownParser()

    assert parser is not None


def test_pdf_parser():
    parser = PDFParser()

    assert parser is not None
