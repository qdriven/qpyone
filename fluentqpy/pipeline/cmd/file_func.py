#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import yaml

from ..cmd import cmd_file


def f_remove():
    os.remove(cmd_file)


def f_add(commands):
    with open(cmd_file, 'w') as f:
        yaml.dump(commands, f, sort_keys=False, indent=2)


def f_syntax_err():
    with open(cmd_file, 'w') as f:
        f.write("error: [][")


def f_scan_err():
    with open(cmd_file, 'w') as f:
        yaml.dump({'err': 'err'}, f)
        yaml.dump("\nerr: arr'", f)


def f_empty():
    with open(cmd_file, 'w') as f:
        f.write("")
