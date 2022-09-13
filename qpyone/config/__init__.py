#!/usr/bin/env python
# python-configuration
# > A library to load configuration parameters hierarchically from multiple sources and formats
#
# [![version](https://img.shields.io/pypi/v/python-configuration)](https://pypi.org/project/python-configuration/)
# ![python](https://img.shields.io/pypi/pyversions/python-configuration)
# ![wheel](https://img.shields.io/pypi/wheel/python-configuration)
# ![license](https://img.shields.io/pypi/l/python-configuration)
# [![build](https://img.shields.io/travis/tr11/python-configuration)](https://travis-ci.org/tr11/python-configuration)
# [![codecov](https://codecov.io/gh/tr11/python-configuration/branch/master/graph/badge.svg)](https://codecov.io/gh/tr11/python-configuration)
# [![Documentation Status](https://readthedocs.org/projects/python-configuration/badge/?version=latest)](https://python-configuration.readthedocs.io/en/latest/?badge=latest)
#
# This library is intended as a helper mechanism to load configuration files hierarchically.  Supported format types are:
#
# * Python files
# * Dictionaries
# * Environment variables
# * Filesystem paths
# * JSON files
# * INI files
# * dotenv type files
#
# and optionally
#
# * YAML files
# * TOML files
# * Azure Key Vault credentials
# * AWS Secrets Manager credentials
# * GCP Secret Manager credentials
#
# ## Installing
#
# To install the library:
#
# ```shell
# pip install python-configuration
# ```
#
# To include the optional TOML and/or YAML loaders, install the optional dependencies `toml` and ` yaml`. For example,
#
# ```shell
# pip install python-configuration[toml,yaml]
# ```
#
# ## Getting started
#
# `python-configuration` converts the various config types into dictionaries with dotted-based keys. For example, given this JSON configuration
#
# ```json
# {
#     "a": {
#         "b": "value"
#     }
# }
# ```
#
# We can use the `config_from_json` method to parse it:
#
# ```python
# from config import config_from_json
#
# cfg = config_from_json("my_config_file.json", read_from_file=True)
# ```
#
# (Similar methods exist for all the other supported configuration formats (eg. `config_from_toml`, etc.).)
#
# We are then able to refer to the parameters in the config above using any of:
#
# ```python
# cfg['a.b']
# cfg['a']['b']
# cfg['a'].b
# cfg.a.b
# ```
#
# and extract specific data types such as dictionaries:
#
# ```python
# cfg['a'].as_dict == {'b': 'value'}
# ```
#
# This is particularly useful in order to isolate group parameters.
# For example, with the JSON configuration
#
# ```json
# {
#   "database.host": "something",
#   "database.port": 12345,
#   "database.driver": "name",
#   "app.debug": true,
#   "app.environment": "development",
#   "app.secrets": "super secret",
#   "logging": {
#     "service": "service",
#     "token": "token",
#     "tags": "tags"
#   }
# }
# ```
#
# one can retrieve the dictionaries as
#
# ```python
# cfg.database.as_dict()
# cfg.app.as_dict()
# cfg.logging.as_dict()
# ```
#
# or simply as
#
# ```python
# dict(cfg.database)
# dict(cfg.app)
# dict(cfg.logging)
# ```
#
# ## Configuration
#
# There are two general types of objects in this library. The first one is the `Configuration`, which represents a single config source.  The second is a `ConfigurationSet` that allows for multiple `Configuration` objects to be specified.
#
# ### Single Config
#
# #### Python Files
#
# To load a configuration from a Python module, the `config_from_python` can be used.
# The first parameter must be a Python module and can be specified as an absolute path to the Python file or as an importable module.
#
# Optional parameters are the `prefix` and `separator`.  The following call
#
# ```python
# config_from_python('foo.bar', prefix='CONFIG', separator='__')
# ```
#
# will read every variable in the `foo.bar` module that starts with `CONFIG__` and replace every occurrence of `__` with a `.`. For example,
#
# ```python
# # foo.bar
# CONFIG__AA__BB_C = 1
# CONFIG__AA__BB__D = 2
# CONF__AA__BB__D = 3
# ```
#
# would result in the configuration
#
# ```python
# {
#     'aa.bb_c': 1,
#     'aa.bb.d': 2,
# }
# ```
#
# Note that the single underscore in `BB_C` is not replaced and the last line is not prefixed by `CONFIG`.
#
# #### Dictionaries
#
# Dictionaries are loaded with `config_from_dict` and are converted internally to a flattened `dict`.
#
# ```python
# {
#     'a': {
#         'b': 'value'
#     }
# }
# ```
#
# becomes
#
# ```python
# {
#     'a.b': 'value'
# }
# ```
#
# #### Environment Variables
#
# Environment variables starting with `prefix` can be read with `config_from_env`:
#
# ```python
# config_from_env(prefix, separator='_')
# ```
#
# #### Filesystem Paths
#
# Folders with files named as `xxx.yyy.zzz` can be loaded with the `config_from_path` function.  This format is useful to load mounted Kubernetes [ConfigMaps](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#populate-a-volume-with-data-stored-in-a-configmap) or [Secrets](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#create-a-pod-that-has-access-to-the-secret-data-through-a-volume).
#
# #### JSON, INI, .env, YAML, TOML
#
# JSON, INI, YAML, TOML files are loaded respectively with
# `config_from_json`,
# `config_from_ini`,
# `config_from_dotenv`,
# `config_from_yaml`, and
# `config_from_toml`.
# The parameter `read_from_file` controls whether a string should be interpreted as a filename.
#
# ###### Caveats
#
# In order for `Configuration` objects to act as `dict` and allow the syntax `dict(cfg)`, the `keys()` method is implemented as the typical `dict` keys. If `keys` is an element in the configuration `cfg` then the `dict(cfg)` call will fail. In that case, it's necessary to use the `cfg.as_dict()` method to retrieve the `dict` representation for the `Configuration` object.
#
# The same applies to the methods `values()` and `items()`.
#
#
# ### Configuration Sets
#
# Configuration sets are used to hierarchically load configurations and merge settings. Sets can be loaded by constructing a `ConfigurationSet` object directly or using the simplified `config` function.
#
# To construct a `ConfigurationSet`, pass in as many of the simple `Configuration` objects as needed:
#
# ```python
# cfg = ConfigurationSet(
#     config_from_env(prefix=PREFIX),
#     config_from_json(path, read_from_file=True),
#     config_from_dict(DICT),
# )
# ```
# The example above will read first from Environment variables prefixed with `PREFIX`, and fallback first to the JSON file at `path`, and finally use the dictionary `DICT`.
#
# The `config` function simplifies loading sets by assuming some defaults.
# The example above can also be obtained by
#
# ```python
# cfg = config(
#     ('env', PREFIX),
#     ('json', path, True),
#     ('dict', DICT),
# )
# ```
#
# or, even simpler if `path` points to a file with a `.json` suffix:
#
# ```python
# cfg = config('env', path, DICT, prefix=PREFIX)
# ```
#
# The `config` function automatically detects the following:
#
# * extension `.py` for python modules
# * dot-separated python identifiers as a python module (e.g. `foo.bar`)
# * extension `.json` for JSON files
# * extension `.yaml` for YAML files
# * extension `.toml` for TOML files
# * extension `.ini` for INI files
# * extension `.env` for dotenv type files
# * filesystem folders as Filesystem Paths
# * the strings `env` or `environment` for Environment Variables
#
# #### Merging Values
#
# `ConfigurationSet` instances are constructed by inspecting each configuration source, taking into account nested dictionaries, and merging at the most granular level.
# For example, the instance obtained from `cfg = config(d1, d2)` for the dictionaries below
#
# ```python
# d1 = {'sub': {'a': 1, 'b': 4}}
# d2 = {'sub': {'b': 2, 'c': 3}}
# ```
#
# is such that `cfg['sub']` equals
#
# ```python
# {'a': 1, 'b': 4, 'c': 3}
# ```
#
# Note that the nested dictionaries of `'sub'` in each of `d1` and `d2` do not overwrite each other, but are merged into a single dictionary with keys from both `d1` and `d2`, giving priority to the values of `d1` over those from `d2`.
#
#
# ###### Caveats
#
# As long as the data types are consistent across all the configurations that are part of a `ConfigurationSet`, the behavior should be straightforward.  When different configuration objects are specified with competing data types, the first configuration to define the elements sets its datatype. For example, if in the example above `element` is interpreted as a `dict` from environment variables, but the JSON file specifies it as anything else besides a mapping, then the JSON value will be dropped automatically.
#
# ## Other Features
#
# ###### String Interpolation
#
# When setting the `interpolate` parameter in any `Configuration` instance, the library will perform a string interpolation step using the [str.format](https://docs.python.org/3/library/string.html#formatstrings) syntax.  In particular, this allows to format configuration values automatically:
#
# ```python
# cfg = config_from_dict({
#     "percentage": "{val:.3%}",
#     "with_sign": "{val:+f}",
#     "val": 1.23456}, interpolate=True)
#
# assert cfg.val == 1.23456
# assert cfg.with_sign == "+1.234560"
# assert cfg.percentage == "123.456%"
# ```
#
# ## Extras
#
# The `config.contrib` package contains extra implementations of the `Configuration` class used for special cases. Currently the following are implemented:
#
# * `AzureKeyVaultConfiguration` in `config.contrib.azure`, which takes Azure Key Vault
#   credentials into a `Configuration`-compatible instance. To install the needed dependencies
#   execute
#
#   ```shell
#   pip install python-configuration[azure]
#   ```
#
# * `AWSSecretsManagerConfiguration` in `config.contrib.aws`, which takes AWS Secrets Manager
#   credentials into a `Configuration`-compatible instance. To install the needed dependencies
#   execute
#
#   ```shell
#   pip install python-configuration[aws]
#   ```
#
# * `GCPSecretManagerConfiguration` in `config.contrib.gcp`, which takes GCP Secret Manager
#   credentials into a `Configuration`-compatible instance. To install the needed dependencies
#   execute
#
#   ```shell
#   pip install python-configuration[gcp]
#   ```
#
# ## Features
#
# * Load multiple configuration types
# * Hierarchical configuration
# * Ability to override with environment variables
# * Merge parameters from different configuration types
#
# ## Contributing :tada:
#
# If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.
#
# See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the details.
#
# ## Links
#
# - Repository: https://github.com/tr11/python-configuration
# - Issue tracker: https://github.com/tr11/python-configuration/issues
# - Documentation: https://python-configuration.readthedocs.io
#
# ## Licensing
#
# The code in this project is licensed under MIT license.
"""python-configuration module."""

from types import ModuleType
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import TextIO
from typing import Union
from typing import cast

import json
import os

from collections.abc import Iterable
from importlib.abc import InspectLoader


try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None
try:
    import toml
except ImportError:  # pragma: no cover
    toml = None

from .fconfig import Configuration
from .fconfig_set import ConfigurationSet
from .fconfig_types import InterpolateEnumType
from .fconfig_types import InterpolateType


def config(
    *configs: Iterable,
    prefix: str = "",
    separator: str | None = None,
    remove_level: int = 1,
    lowercase_keys: bool = False,
    ignore_missing_paths: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> ConfigurationSet:
    """
    Create a :class:`ConfigurationSet` instance from an iterable of configs.

    :param configs: iterable of configurations
    :param prefix: prefix to filter environment variables with
    :param remove_level: how many levels to remove from the resulting config
    :param lowercase_keys: whether to convert every key to lower case.
    :param ignore_missing_paths: whether to ignore failures from missing files/folders.
    :param separator: separator for Python modules and environment variables.
    :param interpolate: whether to apply string interpolation when looking for items

    Note that the :py:attr:`separator` parameter  impacts Python modules and and
    environment variables at the same time. To pass different separators to Python
    modules and environments, use the longer version
    ``('python', 'path-to-module', prefix, separator)``
    and ``('env', prefix, separator)`` .
    """
    instances = []
    default_args: list[str] = [prefix]
    if separator is not None:
        default_args.append(separator)
    default_kwargs: dict[Any, Any] = {
        "lowercase_keys": lowercase_keys,
        # for Configuration Sets, interpolate parameters should be at the Set level
        "interpolate": False,
        "interpolate_type": InterpolateEnumType.STANDARD,
    }

    for config_ in configs:
        if isinstance(config_, dict):
            instances.append(config_from_dict(config_, **default_kwargs))
            continue
        elif isinstance(config_, str):
            if config_.endswith(".py"):
                config_ = ("python", config_, *default_args)
            elif config_.endswith(".json"):
                config_ = ("json", config_, True)
            elif yaml and config_.endswith(".yaml"):
                config_ = ("yaml", config_, True)
            elif toml and config_.endswith(".toml"):
                config_ = ("toml", config_, True)
            elif config_.endswith(".ini"):
                config_ = ("ini", config_, True)
            elif config_.endswith(".env"):
                config_ = ("dotenv", config_, True)
            elif os.path.isdir(config_):
                config_ = ("path", config_, remove_level)
            elif config_ in ("env", "environment"):
                config_ = ("env", *default_args)
            elif all(s and s.isidentifier() for s in config_.split(".")):
                config_ = ("python", config_, *default_args)
            else:
                raise ValueError(f'Cannot determine config type from "{config_}"')

        if not isinstance(config_, (tuple, list)) or len(config_) == 0:
            raise ValueError(
                "configuration parameters must be a list of dictionaries,"
                " strings, or non-empty tuples/lists"
            )
        type_ = config_[0]
        if type_ == "dict":
            instances.append(config_from_dict(*config_[1:], **default_kwargs))
        elif type_ in ("env", "environment"):
            params = list(config_[1:]) + default_args[(len(config_) - 1) :]
            instances.append(config_from_env(*params, **default_kwargs))
        elif type_ == "python":
            if len(config_) < 2:
                raise ValueError("No path specified for python module")
            params = list(config_[1:]) + default_args[(len(config_) - 2) :]
            try:
                instances.append(config_from_python(*params, **default_kwargs))
            except (FileNotFoundError, ModuleNotFoundError):
                if not ignore_missing_paths:
                    raise
        elif type_ == "json":
            try:
                instances.append(config_from_json(*config_[1:], **default_kwargs))
            except FileNotFoundError:
                if not ignore_missing_paths:
                    raise
        elif yaml and type_ == "yaml":
            try:
                instances.append(config_from_yaml(*config_[1:], **default_kwargs))
            except FileNotFoundError:
                if not ignore_missing_paths:
                    raise
        elif toml and type_ == "toml":
            try:
                instances.append(config_from_toml(*config_[1:], **default_kwargs))
            except FileNotFoundError:
                if not ignore_missing_paths:
                    raise
        elif type_ == "ini":
            try:
                instances.append(config_from_ini(*config_[1:], **default_kwargs))
            except FileNotFoundError:
                if not ignore_missing_paths:
                    raise
        elif type_ == "dotenv":
            try:
                instances.append(config_from_dotenv(*config_[1:], **default_kwargs))
            except FileNotFoundError:
                if not ignore_missing_paths:
                    raise
        elif type_ == "path":
            try:
                instances.append(config_from_path(*config_[1:], **default_kwargs))
            except FileNotFoundError:
                if not ignore_missing_paths:
                    raise
        else:
            raise ValueError(f'Unknown configuration type "{type_}"')

    return ConfigurationSet(
        *instances, interpolate=interpolate, interpolate_type=interpolate_type
    )


class EnvConfiguration(Configuration):
    """Configuration from Environment variables."""

    def __init__(
        self,
        prefix: str,
        separator: str = "__",
        *,
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ):
        """
        Constructor.

        :param prefix: prefix to filter environment variables with
        :param separator: separator to replace by dots
        :param lowercase_keys: whether to convert every key to lower case.
        """
        self._prefix = prefix
        self._separator = separator
        super().__init__(
            {},
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )
        self.reload()

    def reload(self) -> None:
        """Reload the environment values."""
        result = {}
        for key, value in os.environ.items():
            if not key.startswith(self._prefix + self._separator):
                continue
            result[
                key[len(self._prefix) :].replace(self._separator, ".").strip(".")
            ] = value
        super().__init__(
            result,
            lowercase_keys=self._lowercase,
            interpolate=self._interpolate,
            interpolate_type=self._interpolate_type,
        )


def config_from_env(
    prefix: str,
    separator: str = "__",
    *,
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`EnvConfiguration` instance from environment variables.

    :param prefix: prefix to filter environment variables with
    :param separator: separator to replace by dots
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return EnvConfiguration(
        prefix,
        separator,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


class PathConfiguration(Configuration):
    """Configuration from a filesytem path."""

    def __init__(
        self,
        path: str,
        remove_level: int = 1,
        *,
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ):
        """
        Constructor.

        :param path: path to read from
        :param remove_level: how many levels to remove from the resulting config
        :param lowercase_keys: whether to convert every key to lower case.
        """
        self._path = path
        self._remove_level = remove_level
        super().__init__(
            {},
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )
        self.reload()

    def reload(self) -> None:
        """Reload the path."""
        path = os.path.normpath(self._path)
        if not os.path.exists(path) or not os.path.isdir(path):
            raise FileNotFoundError()

        dotted_path_levels = len(path.split("/"))
        files_keys = (
            (
                os.path.join(x[0], y),
                ".".join(
                    (x[0].split("/") + [y])[(dotted_path_levels + self._remove_level) :]
                ),
            )
            for x in os.walk(path)
            for y in x[2]
            if not x[0].split("/")[-1].startswith("..")
        )

        result = {}
        for filename, key in files_keys:
            result[key] = open(filename).read()

        super().__init__(
            result,
            lowercase_keys=self._lowercase,
            interpolate=self._interpolate,
            interpolate_type=self._interpolate_type,
        )


def config_from_path(
    path: str,
    remove_level: int = 1,
    *,
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`Configuration` instance from filesystem path.

    :param path: path to read from
    :param remove_level: how many levels to remove from the resulting config
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return PathConfiguration(
        path,
        remove_level,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


class FileConfiguration(Configuration):
    """Configuration from a file input."""

    def __init__(
        self,
        data: str | TextIO,
        read_from_file: bool = False,
        *,
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ):
        """
        Constructor.

        :param data: path to a config file, or its contents
        :param read_from_file: whether to read from a file path or to interpret
               the :attr:`data` as the contents of the file.
        :param lowercase_keys: whether to convert every key to lower case.
        """
        super().__init__(
            {},
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )
        self._reload(data, read_from_file)
        self._data = data if read_from_file and isinstance(data, str) else None

    def _reload(
        self, data: str | TextIO, read_from_file: bool = False
    ) -> None:  # pragma: no cover
        raise NotImplementedError()

    def reload(self) -> None:
        """Reload the configuration."""
        if self._data:  # pragma: no branch
            self._reload(self._data, True)


class JSONConfiguration(FileConfiguration):
    """Configuration from a JSON input."""

    def _reload(self, data: str | TextIO, read_from_file: bool = False) -> None:
        """Reload the JSON data."""
        if read_from_file:
            if isinstance(data, str):
                result = json.load(open(data))
            else:
                result = json.load(data)
        else:
            result = json.loads(cast(str, data))
        self._config = self._flatten_dict(result)


def config_from_json(
    data: str | TextIO,
    read_from_file: bool = False,
    *,
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`Configuration` instance from a JSON file.

    :param data: path to a JSON file or contents
    :param read_from_file: whether to read from a file path or to interpret
           the :attr:`data` as the contents of the JSON file.
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return JSONConfiguration(
        data,
        read_from_file,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


class INIConfiguration(FileConfiguration):
    """Configuration from an INI file input."""

    def __init__(
        self,
        data: str | TextIO,
        read_from_file: bool = False,
        *,
        section_prefix: str = "",
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ):
        self._section_prefix = section_prefix
        super().__init__(
            data=data,
            read_from_file=read_from_file,
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )

    def _reload(self, data: str | TextIO, read_from_file: bool = False) -> None:
        """Reload the INI data."""
        import configparser

        lowercase = self._lowercase

        class ConfigParser(configparser.RawConfigParser):
            def optionxform(self, optionstr: str) -> str:
                return super().optionxform(optionstr) if lowercase else optionstr

        if read_from_file:
            if isinstance(data, str):
                data = open(data).read()
            else:
                data = data.read()
        data = cast(str, data)
        cfg = ConfigParser()
        cfg.read_string(data)
        result = {
            section[len(self._section_prefix) :] + "." + k: v
            for section, values in cfg.items()
            for k, v in values.items()
            if section.startswith(self._section_prefix)
        }
        self._config = self._flatten_dict(result)


def config_from_ini(
    data: str | TextIO,
    read_from_file: bool = False,
    *,
    section_prefix: str = "",
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`Configuration` instance from an INI file.

    :param data: path to an INI file or contents
    :param read_from_file: whether to read from a file path or to interpret
           the :attr:`data` as the contents of the INI file.
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return INIConfiguration(
        data,
        read_from_file,
        section_prefix=section_prefix,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


class DotEnvConfiguration(FileConfiguration):
    """Configuration from a .env type file input."""

    def _reload(self, data: str | TextIO, read_from_file: bool = False) -> None:
        """Reload the .env data."""
        if read_from_file:
            if isinstance(data, str):
                data = open(data).read()
            else:
                data = data.read()
        data = cast(str, data)
        result: dict[str, Any] = dict(
            (y.strip() for y in x.split("=", 1))  # type: ignore
            for x in data.splitlines()
            if x
        )
        self._config = self._flatten_dict(result)


def config_from_dotenv(
    data: str | TextIO,
    read_from_file: bool = False,
    *,
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`Configuration` instance from a .env type file.

    :param data: path to a .env type file or contents
    :param read_from_file: whether to read from a file path or to interpret
           the :attr:`data` as the contents of the INI file.
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return DotEnvConfiguration(
        data,
        read_from_file,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


class PythonConfiguration(Configuration):
    """Configuration from a python module."""

    def __init__(
        self,
        module: str | ModuleType,
        prefix: str = "",
        separator: str = "_",
        *,
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ):
        """
        Constructor.

        :param module: a module or path string
        :param prefix: prefix to use to filter object names
        :param separator: separator to replace by dots
        :param lowercase_keys: whether to convert every key to lower case.
        """
        if isinstance(module, str):
            if module.endswith(".py"):
                import importlib.util

                from importlib import machinery

                spec = cast(
                    machinery.ModuleSpec,
                    importlib.util.spec_from_file_location(module, module),
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader = cast(InspectLoader, spec.loader)
                spec.loader.exec_module(module)
            else:
                import importlib

                module = importlib.import_module(module)
        self._module = module
        self._prefix = prefix
        self._separator = separator
        super().__init__(
            {},
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )
        self.reload()

    def reload(self) -> None:
        """Reload the path."""
        variables = [
            x
            for x in dir(self._module)
            if not x.startswith("__") and x.startswith(self._prefix)
        ]
        result = {
            k[len(self._prefix) :]
            .replace(self._separator, ".")
            .strip("."): getattr(self._module, k)
            for k in variables
        }
        super().__init__(
            result,
            lowercase_keys=self._lowercase,
            interpolate=self._interpolate,
            interpolate_type=self._interpolate_type,
        )


def config_from_python(
    module: str | ModuleType,
    prefix: str = "",
    separator: str = "_",
    *,
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`Configuration` instance from the objects in a Python module.

    :param module: a module or path string
    :param prefix: prefix to use to filter object names
    :param separator: separator to replace by dots
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return PythonConfiguration(
        module,
        prefix,
        separator,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


def config_from_dict(
    data: dict,
    *,
    lowercase_keys: bool = False,
    interpolate: InterpolateType = False,
    interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
) -> Configuration:
    """
    Create a :class:`Configuration` instance from a dictionary.

    :param data: dictionary with string keys
    :param lowercase_keys: whether to convert every key to lower case.
    :param interpolate: whether to apply string interpolation when looking for items
    :return: a :class:`Configuration` instance
    """
    return Configuration(
        data,
        lowercase_keys=lowercase_keys,
        interpolate=interpolate,
        interpolate_type=interpolate_type,
    )


def create_path_from_config(
    path: str, cfg: Configuration, remove_level: int = 1
) -> Configuration:
    """
    Output a path configuration from a :class:`Configuration` instance.

    :param path: path to create the config files in
    :param cfg: :class:`Configuration` instance
    :param remove_level: how many levels to remove
    """
    import os.path

    assert os.path.isdir(path)

    d = cfg.as_dict()
    for k, v in d.items():
        with open(os.path.join(path, k), "wb") as f:
            f.write(str(v).encode())

        cfg = config_from_path(path, remove_level=remove_level)
    return cfg


if yaml is not None:  # pragma: no branch

    class YAMLConfiguration(FileConfiguration):
        """Configuration from a YAML input."""

        def _reload(self, data: str | TextIO, read_from_file: bool = False) -> None:
            """Reload the YAML data."""
            if read_from_file and isinstance(data, str):
                loaded = yaml.load(open(data), Loader=yaml.FullLoader)
            else:
                loaded = yaml.load(data, Loader=yaml.FullLoader)
            if not isinstance(loaded, dict):
                raise ValueError("Data should be a dictionary")
            self._config = self._flatten_dict(loaded)

    def config_from_yaml(
        data: str | TextIO,
        read_from_file: bool = False,
        *,
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ) -> Configuration:
        """
        Return a Configuration instance from YAML files.

        :param data: string or file
        :param read_from_file: whether `data` is a file or a YAML formatted string
        :param lowercase_keys: whether to convert every key to lower case.
        :param interpolate: whether to apply string interpolation when looking for items
        :return: a Configuration instance
        """
        return YAMLConfiguration(
            data,
            read_from_file,
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )


if toml is not None:  # pragma: no branch

    class TOMLConfiguration(FileConfiguration):
        """Configuration from a TOML input."""

        def __init__(
            self,
            data: str | TextIO,
            read_from_file: bool = False,
            *,
            section_prefix: str = "",
            lowercase_keys: bool = False,
            interpolate: InterpolateType = False,
            interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
        ):
            self._section_prefix = section_prefix
            super().__init__(
                data=data,
                read_from_file=read_from_file,
                lowercase_keys=lowercase_keys,
                interpolate=interpolate,
                interpolate_type=interpolate_type,
            )

        def _reload(self, data: str | TextIO, read_from_file: bool = False) -> None:
            """Reload the TOML data."""
            if read_from_file:
                if isinstance(data, str):
                    loaded = toml.load(open(data))
                else:
                    loaded = toml.load(data)
            else:
                data = cast(str, data)
                loaded = toml.loads(data)
            loaded = cast(dict, loaded)

            result = {
                k[len(self._section_prefix) :]: v
                for k, v in self._flatten_dict(loaded).items()
                if k.startswith(self._section_prefix)
            }

            self._config = result

    def config_from_toml(
        data: str | TextIO,
        read_from_file: bool = False,
        *,
        section_prefix: str = "",
        lowercase_keys: bool = False,
        interpolate: InterpolateType = False,
        interpolate_type: InterpolateEnumType = InterpolateEnumType.STANDARD,
    ) -> Configuration:
        """
        Return a Configuration instance from TOML files.

        :param data: string or file
        :param read_from_file: whether `data` is a file or a TOML formatted string
        :param lowercase_keys: whether to convert every key to lower case.
        :param interpolate: whether to apply string interpolation when looking for items
        :return: a Configuration instance
        """
        return TOMLConfiguration(
            data,
            read_from_file,
            section_prefix=section_prefix,
            lowercase_keys=lowercase_keys,
            interpolate=interpolate,
            interpolate_type=interpolate_type,
        )


from .fDynaconf import fsettings


settings = fsettings


def get_all_settings():
    return dir(fsettings)
