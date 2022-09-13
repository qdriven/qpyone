#!/usr/bin/env python
from typing import Dict

from fluentqpy.clients.http.models import HttpLog

from .assertions import assert_that
from .assertions import soft_assertions
from .models import ExpectedResponse


class ResponseValidation:
    def __init__(self, req_log: HttpLog):
        self.req_log = req_log
        self.failed_result = []
        self.passed_result = []

    def verify_all(self, expected: dict):
        expected = ExpectedResponse(**expected)
        with soft_assertions(self.failed_result):
            assert_that(expected.status_code, "check status code").is_equal_to(
                self.req_log.response.status_code
            )
            for k, v in expected.values.items():
                assert_that(v, f"check {k} value ").is_equal_to(
                    get_value(self.req_log.response.data, k)
                )
        assert_that(len(self.failed_result), self.__error_msg()).is_equal_to(0)
        return self

    def __error_msg(self):
        for error in self.failed_result:
            print(error)
        return "".join(self.failed_result)

    def __validate(check_value, expected_exp):
        """
        use assertpy to assert
        todo: need to handle different type,like types
        """

        validator = assert_that(check_value)
        func_param_map = expected_exp.split(" ")
        func = getattr(validator, func_param_map[0])
        params = expected_exp[len(func_param_map[0]) + 1 :].lstrip()
        try:
            if params == "":
                return "success", func()
            return "success", func(params)
        except AssertionError as err:
            return "failed", err
