from uuid import UUID

import pytest

from qpyone.validation import *


@pytest.mark.parametrize(
    ("value",),
    [
        ("2bc1c94f-0deb-43e9-92a1-4775189ec9f8",),
    ],
)
def test_returns_true_on_valid_mac_address(value):
    assert uuid(value)


@pytest.mark.parametrize(
    ("value",),
    [
        (UUID("2bc1c94f-0deb-43e9-92a1-4775189ec9f8"),),
    ],
)
def test_returns_true_on_valid_uuid_object(value):
    assert uuid(value)


@pytest.mark.parametrize(
    ("value",),
    [
        ("2bc1c94f-deb-43e9-92a1-4775189ec9f8",),
        ("2bc1c94f-0deb-43e9-92a1-4775189ec9f",),
        ("gbc1c94f-0deb-43e9-92a1-4775189ec9f8",),
        ("2bc1c94f 0deb-43e9-92a1-4775189ec9f8",),
    ],
)
def test_returns_failed_validation_on_invalid_mac_address(value):
    assert isinstance(uuid(value), ValidationFailure)


@pytest.mark.parametrize(
    ("value",),
    [
        (1,),
        (1.0,),
        (True,),
        (None,),
    ],
)
def test_returns_failed_validation_on_invalid_types(value):
    assert isinstance(uuid(value), ValidationFailure)
