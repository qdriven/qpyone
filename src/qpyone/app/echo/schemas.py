from qpystructs import BaseDataModel


class EchoResponse(BaseDataModel):
    msg: str = "Pong!"
