#!/usr/bin/env python
from mitmproxy.http import HTTPFlow
from plugins.mitm.models import save_http_flow
from qpyone.config.configs import configs


def is_captured_url(url: str):
    url_prefix = configs.mitm.recorded_url.split(",")
    for item in url_prefix:
        if len(item) == 0:
            continue
        if url.startswith(item):
            return True
    return False


class PRecorder:
    def __init__(self):
        print("api recorder initialized ....")

    def http_connect(self, flow: HTTPFlow):
        print("http_connect state")
        # print(flow)

    def requestheaders(self, flow: HTTPFlow):
        print("request headers state")
        # print(flow)

    def request(self, flow: HTTPFlow):
        pass

    def responseheaders(self, flow: HTTPFlow):
        print("respones headers state")

    def response(self, flow: HTTPFlow):
        """
        extract both request and response
        into local database/sqlite
        then update to center database
        Args:
            flow:

        Returns:

        """
        if (
            is_captured_url(flow.request.url)
            and flow.request.method.lower() != "options"
        ):
            save_http_flow(flow)

    def error(self, flow: HTTPFlow):
        print("error state")

    # def tcp_start(self, flow: TCPFlow):
    #     print("tcp start state")
    #
    # def tcp_message(self, flow: TCPFlow):
    #     print("tcp message state")
    #
    # def tcp_error(self, flow: TCPFlow):
    #     print("tcp error state")
    #
    # def tcp_end(self, flow: TCPFlow):
    #     print("tcp send state")

    # def websocket_handshake(self, flow: HTTPFlow):
    #     print("websocket send state")


addons = [PRecorder()]
