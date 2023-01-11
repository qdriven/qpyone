#!/usr/bin/env python
from qpyone.case_server.pytest_runner import PytestRunner
from qpyone.case_server.pytest_runner import RunCaseOption


runner = PytestRunner()


def test_run():

    runner.run(RunCaseOption(service_name="iotools"))
