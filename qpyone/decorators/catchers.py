#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Callable
from typing import Union

import contextlib
import logging


@contextlib.contextmanager
def catches(
    *exceptions,
    raises: Union[BaseException, Callable[[Exception], BaseException]],
    logger=None,
):
    """封装转换错误类。transfer exceptions to a different type.

    Examples::

        with self.assertRaises(IOError), catches(ValueError, TypeError, raises=IOError()):
            raise ValueError('should wrap this error')

        @catches(raises=get_validation_error, log=True)
        def raise_io_error():
            raise ValueError('should wrap this error')
    """
    exceptions = exceptions or (Exception,)
    try:
        yield
    except exceptions as ex:
        if callable(raises):
            raises = raises(ex)
        if logger:
            log_error(logger, raises)
        raise raises from ex


def log_error(logger, message, *args, exc_info=True, **kwargs):
    """记录错误日志的快捷方式，顺带支持 Sentry。log error, supports sentry detail trace.

    Examples::

        log_error(logger, ex)
        log_error(__name__, 'this message will show on sentry')
    """
    if isinstance(logger, str):
        logger = logging.getLogger(logger)
    if isinstance(message, Exception) or exc_info:
        logger.exception(message, *args, **kwargs)
    else:
        # https://github.com/getsentry/raven-python/blob/master/docs/integrations/logging.rst#usage
        logger.error(message, *args, extra={"stack": True}, **kwargs)
