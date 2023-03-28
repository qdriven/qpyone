from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Type

import inspect

from abc import ABC

from qpyone.base import GenericDataModel
from qpyone.runner.meta.meta_utils import create_args_class
from qpyone.runner.meta.meta_utils import get_return_result_hint


class ServiceMeta(GenericDataModel):
    service_name: str
    impl_cls: str = None


class MethodMeta(GenericDataModel):
    service_name: str = None
    method_name: str
    impl_method: Callable = None
    arguments: Any
    result_hint: Any


SPELL_NAME = "__spell_name__"


class Service(ABC):
    __service_meta__: ServiceMeta = None
    __methods_meta__: Dict[str, MethodMeta] = None

    @classmethod
    def _service_meta(cls) -> ServiceMeta:
        return cls.__service_meta__

    @classmethod
    def _method_meta(cls, method_name) -> MethodMeta:
        return cls.__methods_meta__[method_name]

    @classmethod
    def name(cls):

        if hasattr(cls, SPELL_NAME):
            return getattr(cls, SPELL_NAME)[0]
        else:
            return cls.__name__


## 一种路由的方式
## service/method args: {} 数据
## context, inputdata,invocation
## plugin 模式
## 执行脚本方式


def service_metalize(cls: Type[Service]):
    service_name = cls.name()
    cls.__service_meta__ = ServiceMeta(service_name=service_name)
    method_meta = {}
    all_methods = inspect.getmembers(cls, predicate=lambda m: inspect.isfunction(m))
    for name, method in all_methods:
        print(name)
        print(method)
        skel_name, arg_skel_names = getattr(method, SPELL_NAME)
        route_prefix = ".".join([service_name, name])
        method_meta[route_prefix] = MethodMeta(
            name=name,
            service_name=service_name,
            arguments=create_args_class(method, name, service_name),
            result_hint=get_return_result_hint(method),
        )
    cls.__methods_meta__ = method_meta


def spell(name: str = None, arg_names: List[str] = None):
    def spellize(target):
        if not (
            (inspect.isclass(target) and issubclass(target, Service))
            or (inspect.isfunction(target) and "." in target.__qualname__)
        ):
            raise TypeError("not supported type")
        if name is None:
            spell_name = target.__name__
        else:
            spell_name = name
        setattr(target, SPELL_NAME, (spell_name, arg_names))
        if inspect.isclass(target):
            service_metalize(target)
        return target

    return spellize


def method_metalize(func):
    raise NotImplemented("not implemented yet")


# @spell
# class ServiceA(Service):
#
#     @spell(name,args=[])
#     def spell_func(self):
#         pass
