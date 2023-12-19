#!/usr/bin/env python
from typing import Any

from qpyone.clients.http.client import BaseHttpClient
from qpyone.clients.http.client import HttpClientOption


class HttpServiceContainer:
    cls_dic: dict[type, Any]
    named_dic: dict[str, Any]

    def __init__(self, invoker: BaseHttpClient = None):
        """
        init sdk for register
        :param invoker:
        """
        self.cls_dic = {}
        self.named_dic = {}
        self.invoker: BaseHttpClient = invoker

    def register(self, type: Any, **kwargs):
        """
        注册到SDK容器
        Args:
            type: class type
            **kwargs:
                - name:
                - scope: singleton, not used yet
        Returns:

        """
        print("start to inject to Container")
        if self.cls_dic.get(type) is None:
            instance = type.create(invoker=self.invoker)
            self.cls_dic[type] = instance
            self.named_dic[type.__name__.lower()] = instance
        return type

    def get(self, type: Any) -> Any:
        self.cls_dic[type].invoker = self.invoker
        return self.cls_dic[type]

    def __getitem__(self, name) -> Any:
        if self.named_dic[name]:
            return self.named_dic[name]
        else:
            raise KeyError(f"{name} service is not registered")

    def http_options(self, options: HttpClientOption):
        self.invoker.options = options
        return self


sdk = HttpServiceContainer()
