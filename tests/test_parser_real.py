from research_navigator.ingest.parser import (
    MarkdownParser,
)


def test_markdown_parse(
    tmp_path,
):
    file = tmp_path / "sample.md"

    file.write_text(
        "# Introduction\nHello World\n\n# Method\nTesting",
        encoding="utf-8",
    )

    parser = MarkdownParser()

    document = parser.parse(
        str(file),
        "doc1",
    )

    assert document.doc_id == "doc1"

    assert len(document.sections) == 2

    assert document.sections[0].title == "Introduction"

    assert document.sections[1].title == "Method"


def test_root_section(
    tmp_path,
):
    file = tmp_path / "simple.md"

    file.write_text(
        "hello world",
        encoding="utf-8",
    )

    parser = MarkdownParser()

    document = parser.parse(
        str(file),
        "doc2",
    )

    assert document.doc_id == "doc2"

    assert len(document.sections) == 1

    assert document.sections[0].title == "ROOT"


def test_multiple_sections(
    tmp_path,
):
    file = tmp_path / "multi.md"

    file.write_text(
        "# A\nText A\n\n# B\nText B\n\n# C\nText C",
        encoding="utf-8",
    )

    parser = MarkdownParser()

    document = parser.parse(
        str(file),
        "doc3",
    )

    assert len(document.sections) == 3

    assert document.sections[2].title == "C"
