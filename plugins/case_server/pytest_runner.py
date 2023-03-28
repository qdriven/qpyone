#!/usr/bin/env python
import pytest

from qpyone.base import BaseDataModel


class RunCaseOption(BaseDataModel):
    service_name: str | None


## Tests/Service/locations
## ServiceName
class PytestRunner:
    def __init__(self):
        pass

    # TODO: add pytest json result plugin to return the result
    def run(self, case_options: RunCaseOption):
        service_test_file_name = f"test_{case_options.service_name}.py"
        return pytest.main([service_test_file_name])
