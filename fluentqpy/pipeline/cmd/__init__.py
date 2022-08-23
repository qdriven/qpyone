#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import yaml

EXCEPTIONS = (yaml.reader.ReaderError,
              yaml.MarkedYAMLError,
              yaml.YAMLError)

PATTERN = "<[0-9]>"

cmd_file = os.getenv("cmd_file") if os.getenv("cmd_file") else 'cmd.yaml'
