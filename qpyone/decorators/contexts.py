#!/usr/bin/env python
# -*- coding:utf-8 -*-
import contextlib


class EmptyContextManager(contextlib.ContextDecorator):
    """empty context manager."""

    def __init__(self):
        """do nothing"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Always throw exception"""
        return False
