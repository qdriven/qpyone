class DispatcherMixin:
    pass


class BaseDispatcher:
    def __init__(self):
        self._registers = {}

    def call(self):
        pass
