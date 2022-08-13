from fluentqpy.config import settings


def test_configuration_loaded():
    assert settings.log_level == 'INFO'
