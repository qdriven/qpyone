from .domain import Bar, Foo
from .services import FooPrinter


def controller1(foo: Foo):
    return foo.value1, foo.value2


def controller2(foo_printer: FooPrinter):
    return foo_printer.print()


def controller3(bar: Bar):
    return bar.__dict__
