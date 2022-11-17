#!/usr/bin/env python

from mitmproxy.http import HTTPFlow


class PRecorder:
    def __init__(self):
        print("api recorder initialized ....")

    def request(self, flow: HTTPFlow):
        if flow.request.url.startswith("https://matrix-api"):
            print("request received ")
            print(flow.request.url)
            print(flow.request.method)
            print(flow.request.content)
            print(flow.request.headers)
            # todo: server to sqlite

    def response(self, flow: HTTPFlow):
        """
        extract both request and response
        into local database/sqlite
        then update to center database
        Args:
            flow:

        Returns:

        """
        if flow.request.url.startswith("https://matrix-api"):
            print(flow.response.content)


addons = [PRecorder()]
