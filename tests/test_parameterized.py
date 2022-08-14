import pytest
from qpyplugins.pytp import more_params

data = more_params.fixture('one', 'two')


def test_options():
    fixture = more_params.fixture(name='override')
    assert fixture._pytestfixturefunction.name == 'override'
    assert more_params(lambda x='': x, scope='module').kwargs == {'scope': 'module'}


def test_fixture(data):
    assert data in ('one', 'two')


@more_params
def test_single(name='abc'):
    assert name in set('abc')


@more_params.zip
def test_zip(name='abc', value=range(3)):
    assert (value, name) in enumerate('abc')


@more_params.product
def test_product(name='abc', value=range(3)):
    assert name in set('abc') and value in (0, 1, 2)


def test_error(name='abc', value=range(3)):
    with pytest.raises(ValueError):

        @more_params
        def test(name=(), value=()):
            pass
