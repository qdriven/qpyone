#!/usr/bin/env python
from plugins.case_server.pytest_runner import PytestRunner
from plugins.case_server.pytest_runner import RunCaseOption


runner = PytestRunner()


def test_run():

    runner.run(RunCaseOption(service_name="iotools"))
