#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pathlib
import sys

from ..loader import register

# append an additional location where to look for Python modules
sys.path.append(f"{pathlib.Path(__file__).parent.resolve()}/dependencies")


from . import misc

register(sys.modules[__name__], {"id": __name__, "name": "demo", "actions": {"get_public_ip": main.get_public_ip}})
