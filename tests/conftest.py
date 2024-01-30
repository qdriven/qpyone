import os

import pytest
from qpybase import settings


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev",
                     help="Environment to run tests in")


# provider env value in pytest
def env(request):
    return request.config.getoption("-—env")


def ensure_env_settings(env_name: str):
    env_switcher_key = settings.ENV_SWITCHER_FOR_DYNACONF
    os.environ[env_switcher_key] = env_name
    settings.reload()


@pytest.fixture(scope="session", autouse=True)
def setup_environment_setting(request):
    env_name = request.config.getoption("--env")
    ensure_env_settings(env_name)
