from qpyone.base import GenericDataModel


class Request(GenericDataModel):
    pass


class GetRequest(GenericDataModel):
    id: str = None
    handle: str = None


class CreateRequest(Request):
    id: str = None
    handle: str = None


class UpdateRequest(Request):
    id: str = None
    handle: str = None


class IdentifierRequest(Request):
    id: str = None
    handle: str = None


class ListRequest(Request):
    pass


class DeleteRequest(Request):
    id: str
