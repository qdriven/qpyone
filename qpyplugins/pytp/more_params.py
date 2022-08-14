import inspect
import itertools
from functools import partial
import pytest

def more_parameterized(func, combine=None, **kwargs):
    """Decorate a function with combined parameters."""
    argspec = inspect.getfullargspec(func)
    params = dict(zip(reversed(argspec.args), reversed(argspec.defaults)))
    func.__defaults__ = ()  # pytp ignores params with defaults
    if combine is None:
        (args,) = params.items()  # multiple keywords require combine function, e.g., zip
    else:
        args = ','.join(params), combine(*params.values())
    return pytest.mark.parametrize(*args, **kwargs)(func)


def fixture(*params, **kwargs):
    return pytest.fixture(params=params, **kwargs)(lambda request: request.param)


more_parameterized.fixture = fixture
more_parameterized.zip = partial(more_parameterized, combine=zip)
more_parameterized.product = partial(more_parameterized, combine=itertools.product)
