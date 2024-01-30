import os

from qpyone.constants import get_base_dir, BASE_DIR


def test_get_base_dir():
    print(get_base_dir())
    print(BASE_DIR)
    print(os.path.join(BASE_DIR, "templates"))
