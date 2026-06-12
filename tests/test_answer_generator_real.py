from unittest.mock import Mock

from research_navigator.retrieve.answer_generator import (
    AnswerGenerator,
)


def test_generate_answer():
    generator = AnswerGenerator()

    generator.model = Mock()

    generator.model.invoke.return_value.content = "Generated answer"

    fake_point = Mock()

    fake_point.payload = {
        "title": "Paper",
        "section_title": "ABSTRACT",
        "text": "Transformer model",
    }

    answer = generator.generate(
        "What is transformer?",
        [{"point": fake_point}],
    )

    assert answer == "Generated answer"
