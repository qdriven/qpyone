from fluentqpy.config import settings


def test_configuration_loaded():
    assert settings.log_level == 'INFO'
    assert settings.db == 'test_db'
    settings.structure.test = "http://localhost:7077"
