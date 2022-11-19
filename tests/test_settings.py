from qpyone.config import configs


def test_configuration_loaded():
    assert configs.log_level == "INFO"
    assert configs.db == "test_db"
    configs.structure.test = "http://localhost:7077"
