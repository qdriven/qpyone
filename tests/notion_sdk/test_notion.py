#!/usr/bin/env python
# -*- coding:utf-8 -*-
from fsdk.notion.notion import notion_sdk, async_notion_sdk
from fluentqpy.config import settings


class TestNotionSdk:

    def test_secret_loading(self):
        assert settings.notion_token is not None

    def test_notion_sdk(self):
        assert notion_sdk is not None
        assert async_notion_sdk is not None

    def test_notion_database(self):
        assert notion_sdk.databases is not None
        result = notion_sdk.databases.list()
        print(result)

    def test_search(self):
        result = notion_sdk.search()
        print(result)

    def test_create_db(self):
        pass
