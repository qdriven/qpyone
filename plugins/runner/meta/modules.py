from typing import Dict
from typing import Optional

import sys


_loaded_modules: Dict[str, Optional[str]] = {}


def _refresh_loaded_modules():
    for module in sys.modules.values():
        if hasattr(module, "__file__") and module.__file__ is not None:
            _loaded_modules[module.__file__] = module.__name__


def retrieve_module_name(*, path: str) -> Optional[str]:
    if path not in _loaded_modules:
        _refresh_loaded_modules()
        if path not in _loaded_modules:
            _loaded_modules[path] = None
    return _loaded_modules[path]
