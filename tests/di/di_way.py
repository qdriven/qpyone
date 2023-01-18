#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


class ApiClient:
    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected


class Service:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client  # <-- dependency is injected

    def do_it(self):
        print(self)

    def __str__(self):
        return "{}.{}".format(self.api_client.api_key, self.api_client.timeout)


def main(service: Service) -> None:  # <-- dependency is injected
    service.do_it()


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY", default="test"),
                timeout=int(os.getenv("TIMEOUT", default="10")),
            ),
        ),
    )
