from qpyone.clients.http.models import HttpMethod
from qpyone.core.service import BaseRpcService


class HttpMethodTestService(BaseRpcService):
    base_url = "http://httpbin.org/"

    def get(self):
        req = self._make_request_model(method="get", path="/get")
        return self.invoker.request(req)

    def delete(self):
        req = self._make_request_model(method="delete", path="/delete")
        return self.invoker.request(req)

    def put(self):
        req = self._make_request_model(method="put", path="/put")
        return self.invoker.request(req)

    def post(self):
        req = self._make_request_model(method=HttpMethod.POST.value, path="/post")
        return self.invoker.request(req)
