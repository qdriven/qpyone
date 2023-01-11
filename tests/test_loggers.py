from qpyone.core import qpy_logger


def test_flogger():
    qpy_logger.log("test {}", "test_var")
