from qpyone.core import loggers


def test_flogger():
    loggers.log("test {}", "test_var")
