import uvicorn
from fastapi import FastAPI

from qpyone.app.di.autowire import Autowirer
from tests.example.controllers import *
from tests.example.domain import Foo, Bar
from tests.example.services import FooPrinter

aw = Autowirer()


@aw.register
def int_factory() -> int:
    return 10


@aw.register
@aw.autowire
def float_factory(val: int) -> float:
    return 10.0 * val


aw.register(aw.autowire(Foo))
aw.register(aw.autowire(FooPrinter))


@aw.register
@aw.autowire
def bar_factory(foo: Foo) -> Bar:
    return Bar(foo.value1 + 1, foo.value2 + 2)


app = FastAPI()
app.add_api_route("/1", aw.autowire(controller1))
app.add_api_route("/2", aw.autowire(controller2))
app.add_api_route("/3", aw.autowire(controller3))

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
