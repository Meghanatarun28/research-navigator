from research_navigator.ingest.parser import (
    PDFParser,
)


def test_pdf_parser_creation():
    parser = PDFParser()

    assert parser is not None
