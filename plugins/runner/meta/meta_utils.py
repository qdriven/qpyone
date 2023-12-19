from typing import Any
from typing import List
from typing import Type

import inspect
import sys

from pydantic.fields import Field
from qpybase import GenericDataModel


def export_all(module_name: str, given_type: Type) -> List:
    names = []
    for name, obj in inspect.getmembers(sys.modules[module_name]):
        if inspect.isclass(obj) and issubclass(obj, given_type):
            names.append(obj.__name__)
    return names


def get_return_result_hint(method: callable) -> Any:
    return inspect.getfullargspec(method).annotations["return"]


def create_args_class(
    method: callable, method_name: str, method_arg_names: List[str]
) -> Type:
    """
    create dynamic class for request
    :param method:
    :param method_name:
    :param method_arg_names:
    :return:
    """
    method_specs = inspect.getfullargspec(method)
    arg_names = method_specs[1:]

    cls_attrs = {"__module__": method.__module__}
    arg_annos = {}
    for index in range(len(arg_names)):
        cls_attrs[arg_names[index]] = Field(None, alias=method_arg_names[index])
        arg_annos[arg_names[index]] = method_specs.annotations[arg_names[index]]
    if len(cls_attrs) > 0:
        cls_attrs["__annotations__"] = arg_annos

    service_cls_name, _ = method.__qualname__.split(".")
    cls_name = f"{service_cls_name}.{upper_first(method_name)}Arguments"
    cls = type(cls_name, (GenericDataModel,), cls_attrs)
    return cls


def upper_first(string: str) -> str:
    return string[0].upper() + string[1:]
