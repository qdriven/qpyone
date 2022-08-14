from spell import __version__
from spell.config import settings


def test_version():
    assert __version__ == '0.1.0'


def test_configuration_loaded():
    assert settings.test_name == 'test'
    assert settings.mock_db.port == "7453"
    assert settings.mock_db.attr == "default"
    assert settings.server.port == 9091
    assert settings.server.database.port == 7450
