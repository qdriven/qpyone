from qpyone.config import configs


def test_configuration_loaded():
    assert configs.log_level == "INFO"
    configs.structure.test = "http://localhost:7077"
    assert configs.mitm.recorded_url == "https://matrix-api,"
