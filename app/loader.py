#!/usr/bin/env python
# -*- coding:utf-8 -*-
import importlib
import io
import os
import shutil
import sys
import uuid
import zipfile
from typing import Any, Callable, List, Mapping, Union

from .settings import settings

PLUGIN_DIRS = [settings.local_dynamic_modules_path, settings.dynamic_modules_path]

for path in PLUGIN_DIRS:
    sys.path.append(path)

try:
    os.mkdir(settings.dynamic_modules_path)
except FileExistsError:
    pass


class Registry:
    _registry: Mapping[str, Mapping[str, Any]] = {}
    _id_to_name: Mapping[str, str] = {}

    def format_module_info(self, module_item: Mapping[str, Any]) -> Mapping[str, Any]:
        return {
            "id": module_item["id"],
            "name": module_item["name"],
            "actions": list(module_item.get("actions", {}).keys()),
        }

    def modules(self) -> List[Mapping[str, Any]]:
        return [self.format_module_info(module_items) for module_items in self._registry.values()]

    def get_module_details_by_id(self, module_id: str) -> Mapping[str, Any]:
        name = self._id_to_name.get(module_id)
        return self.format_module_info(self._registry[name])

    def package_refs(self) -> List[Any]:
        return [module["module"] for module in self._registry.values()]

    def get(self, module_name: str, default: Any = None) -> Any:
        if default is None:
            return self._registry[module_name]
        return self._registry.get(module_name, default)

    def add(self, *, module: Any, name: str, package_id: str, actions: Mapping[str, Callable]) -> None:
        self._registry[name] = {"id": package_id, "name": name, "module": module, "actions": actions}
        self._id_to_name[package_id] = name

    def get_action(self, module_name: str, action: str) -> Callable:
        return self._registry[module_name]["actions"][action]


registry = Registry()


def register(module, details):

    name = details.pop("name")
    package_id = details.pop("id")

    current = registry.get(name, {})

    if current and current["id"] != package_id:
        shutil.rmtree(path=os.path.join(settings.dynamic_modules_path, current["id"]))

    registry.add(
        module=module,
        name=name,
        package_id=package_id,
        actions=details.get("actions", {}),
    )


def reload_plugins() -> None:
    for module in registry.package_refs():
        importlib.reload(module)


def register_modules(dynamic_modules_path: str) -> None:

    modules = []
    for (dirpath, dirnames, filenames) in os.walk(dynamic_modules_path):
        modules.extend(dirnames)
        break

    for module_name in modules:
        if "__" in module_name:
            continue
        importlib.import_module(f"{module_name}")


def load_plugins() -> None:
    for module_path in PLUGIN_DIRS:
        register_modules(module_path)


def extract_zip(file: Union[str, bytes], extract_path: str) -> None:

    zip_file: Union[io.BytesIO, str]

    if isinstance(file, str):
        zip_file = file

    if isinstance(file, bytes):
        zip_file = io.BytesIO(file)

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_path)


def install_module(module: bytes) -> Mapping[str, Any]:
    module_uuid = str(uuid.uuid4()).replace("-", "")
    extract_zip(module, os.path.join(settings.dynamic_modules_path, module_uuid))
    load_plugins()
    return registry.get_module_details_by_id(module_uuid)

