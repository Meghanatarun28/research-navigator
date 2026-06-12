from research_navigator.config.settings import (
    settings,
)


def test_settings_loaded():
    assert settings.qdrant_port == 6333
