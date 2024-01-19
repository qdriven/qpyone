class Foo:
    def __init__(self, value1: int, value2: float):
        self.value1 = value1
        self.value2 = value2


class Bar:
    def __init__(self, arg1, arg2):
        self._arg1, self._arg2 = arg1, arg2
