from __future__ import annotations

import os
import random
import secrets
import string
from typing import Dict, Optional

import aiohttp
from aiohttp import BaseConnector

from qpyone.app.gpt4.sp.base import constants
from qpyone.app.gpt4.sp.base.errors import MissingRequirementsError, \
    MissingAiohttpSocksError
from qpyone.app.gpt4.sp.base.schemas import Cookies

try:
    from platformdirs import user_config_dir

    has_platformdirs = True
except ImportError:
    has_platformdirs = False
try:
    from browser_cookie3 import (
        chrome, chromium, opera, opera_gx,
        brave, edge, vivaldi, firefox,
        _LinuxPasswordManager, BrowserCookieError
    )

    has_browser_cookie3 = True
except ImportError:
    has_browser_cookie3 = False


# Global variable to store cookies
_cookies: Dict[str, Cookies] = {}

if has_browser_cookie3 and os.environ.get('DBUS_SESSION_BUS_ADDRESS') == "/dev/null":
    _LinuxPasswordManager.get_password = lambda a, b: b"secret"


def get_cookies(domain_name: str = '', raise_requirements_error: bool = True) -> Dict[
    str, str]:
    """
    Load cookies for a given domain from all supported browsers and cache the results.

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    if domain_name in _cookies:
        return _cookies[domain_name]

    cookies = load_cookies_from_browsers(domain_name, raise_requirements_error)
    _cookies[domain_name] = cookies
    return cookies


def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    if cookies:
        _cookies[domain_name] = cookies
    else:
        _cookies.pop(domain_name)


def load_cookies_from_browsers(domain_name: str,
                               raise_requirements_error: bool = True) -> Cookies:
    """
    Helper function to load cookies from various browsers.

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    if not has_browser_cookie3:
        if raise_requirements_error:
            raise MissingRequirementsError('Install "browser_cookie3" package')
        return {}
    cookies = {}
    for cookie_fn in [_qpyone, chrome, chromium, opera, opera_gx, brave, edge, vivaldi,
                      firefox]:
        try:
            cookie_jar = cookie_fn(domain_name=domain_name)
            if len(cookie_jar) and constants.logging:
                print(f"Read cookies from {cookie_fn.__name__} for {domain_name}")
            for cookie in cookie_jar:
                if cookie.name not in cookies:
                    cookies[cookie.name] = cookie.value
        except BrowserCookieError:
            pass
        except Exception as e:
            if constants.logging:
                print(
                    f"Error reading cookies from {cookie_fn.__name__} for {domain_name}: {e}")
    return cookies


def _qpyone(domain_name: str) -> list:
    """
    Load cookies from the 'qpyone' browser (if exists).

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        list: List of cookies.
    """
    if not has_platformdirs:
        return []
    user_data_dir = user_config_dir("qpyone")
    cookie_file = os.path.join(user_data_dir, "Default", "Cookies")
    return [] if not os.path.exists(cookie_file) else chrome(cookie_file, domain_name)


def get_random_string(length: int = 10) -> str:
    """
    Generate a random string of specified length, containing lowercase letters and digits.

    Args:
        length (int, optional): Length of the random string to generate. Defaults to 10.

    Returns:
        str: A random string of the specified length.
    """
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(length)
    )


def get_random_hex() -> str:
    """
    Generate a random hexadecimal string of a fixed length.

    Returns:
        str: A random hexadecimal string of 32 characters (16 bytes).
    """
    return secrets.token_hex(16).zfill(32)


def get_connector(connector: BaseConnector = None, proxy: str = None) -> Optional[
    BaseConnector]:
    if proxy and not connector:
        try:
            from aiohttp_socks import ProxyConnector
            connector = ProxyConnector.from_url(proxy)
        except ImportError:
            raise MissingAiohttpSocksError(
                'Install "aiohttp_socks" package for proxy support')
    if connector is None:
        return aiohttp.TCPConnector(ssl=False)
    return connector
