#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Dict, Any

from spell.clients.http.client import BaseHttpClient, HttpClient, HttpClientOption


class HttpSdk:
    cls_dic: Dict[type, Any]
    named_dic: Dict[str, Any]

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


sdk = HttpSdk()
