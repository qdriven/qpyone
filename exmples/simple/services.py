from .domain import Foo


class FooPrinter:
    def __init__(self, foo: Foo):
        self._foo = foo

    def print(self):
        return f"value1={self._foo.value1}  value2={self._foo.value2}"
