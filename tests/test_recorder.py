#!/usr/bin/env python
import pytest

from plugins.mitm.recorder import is_captured_url


@pytest.mark.skip
def test_is_captured_url():
    result = is_captured_url(
        "https://twitter.com/i/api/fleets/v1/avatar_content?user_ids=1400005167525793793&only_spaces=true"
    )
    print(result)
