#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

from spell.clients.http.typing import SyncAsync
from spell.clients.service import BaseRpcService
from spell.utilities.misc import pick_by_keys


class BlocksChildrenEndpoint(BaseRpcService):

    def append(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Create and append new children blocks to the block using the ID specified.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/patch-block-children)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"blocks/{block_id}/children",
            method="PATCH",
            body=pick_by_keys(kwargs, "children"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )

    def list(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Return a paginated array of child [block objects](https://developers.notion.com/reference/block) contained in the block.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/get-block-children)*
        """  # noqa: E501
        return self.invoker.request(
            
            path=f"blocks/{block_id}/children",
            method="GET",
            query=pick_by_keys(kwargs, "start_cursor", "page_size"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )


class BlocksEndpoint(BaseRpcService):

    def __init__(self, invoker: Any, **kwargs: Any) -> None:
        super(BlocksEndpoint, self).__init__(invoker, **kwargs)
        self.children = BlocksChildrenEndpoint(invoker, **kwargs)

    def retrieve(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Retrieve a [Block object](https://developers.notion.com/reference/block) using the ID specified.
        *[🔗 Endpoint documentation](https://developers.notion.com/reference/retrieve-a-block)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"blocks/{block_id}", method="GET", auth=kwargs.get("auth")
        )

    def update(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Update the content for the specified `block_id` based on the block type.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/update-a-block)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"blocks/{block_id}",
            method="PATCH",
            body=pick_by_keys(
                kwargs,
                "embed",
                "type",
                "archived",
                "bookmark",
                "image",
                "video",
                "pdf",
                "file",
                "audio",
                "code",
                "equation",
                "divider",
                "breadcrumb",
                "table_of_contents",
                "link_to_page",
                "table_row",
                "heading_1",
                "heading_2",
                "heading_3",
                "paragraph",
                "bulleted_list_item",
                "numbered_list_item",
                "quote",
                "to_do",
                "toggle",
                "template",
                "callout",
                "synced_block",
                "table",
            ),
            auth=kwargs.get("auth"),base_url=self.base_url
        )

    def delete(self, block_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Set a [Block object](https://developers.notion.com/reference/block), including page blocks, to `archived: true`.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/delete-a-block)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"blocks/{block_id}",
            method="DELETE",
            auth=kwargs.get("auth"),base_url=self.base_url
        )


class DatabasesEndpoint(BaseRpcService):
    def list(self, **kwargs: Any) -> SyncAsync[Any]:
        """List all [Databases](https://developers.notion.com/reference/database) shared with the authenticated integration.

        > ⚠️  **Deprecated endpoint**

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/get-databases)*
        """  # noqa: E501
        return self.invoker.request(
            path="databases",
            method="GET",
            query=pick_by_keys(kwargs, "start_cursor", "page_size"),
            auth=kwargs.get("auth"),base_url=self.base_url,
            headers={"Notion-Version": "2021-08-16"}
        )

    def query(self, database_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Get a list of [Pages](https://developers.notion.com/reference/page) contained in the database.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/post-database-query)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"databases/{database_id}/query",
            method="POST",
            body=pick_by_keys(kwargs, "filter", "sorts", "start_cursor", "page_size"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )

    def retrieve(self, database_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Retrieve a [Database object](https://developers.notion.com/reference/database) using the ID specified.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/post-database-query)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"databases/{database_id}", method="GET", auth=kwargs.get("auth")
        )

    def create(self, **kwargs: Any) -> SyncAsync[Any]:
        """Create a database as a subpage in the specified parent page.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/create-a-database)*
        """  # noqa: E501
        return self.invoker.request(
            path="databases",
            method="POST",
            body=pick_by_keys(kwargs, "parent", "title", "properties", "icon", "cover"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )

    def update(self, database_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Update an existing database as specified by the parameters.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/update-a-database)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"databases/{database_id}",
            method="PATCH",
            body=pick_by_keys(kwargs, "properties", "title", "icon", "cover"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )


class PagesPropertiesEndpoint(BaseRpcService):
    def retrieve(self, page_id: str, property_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Retrieve a `property_item` object for a given `page_id` and `property_id`.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/retrieve-a-page-property)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"pages/{page_id}/properties/{property_id}",
            method="GET",
            auth=kwargs.get("auth"),base_url=self.base_url,
            query=pick_by_keys(kwargs, "start_cursor", "page_size"),
        )


class PagesEndpoint(BaseRpcService):
    def __init__(self, invoker: Any, **kwargs: Any) -> None:
        super(PagesEndpoint, self).__init__(invoker, **kwargs)
        self.properties = PagesPropertiesEndpoint(invoker, **kwargs)

    def create(self, **kwargs: Any) -> SyncAsync[Any]:
        """Create a new page in the specified database or as a child of an existing page.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/post-page)*
        """  # noqa: E501
        return self.invoker.request(
            path="pages",
            method="POST",
            body=pick_by_keys(kwargs, "parent", "properties", "children", "icon", "cover"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )

    def retrieve(self, page_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Retrieve a [Page object](https://developers.notion.com/reference/page) using the ID specified.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/retrieve-a-page)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"pages/{page_id}", method="GET", auth=kwargs.get("auth")
        )

    def update(self, page_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Update [page property values](https://developers.notion.com/reference/page#property-value-object) for the specified page.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/patch-page)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"pages/{page_id}",
            method="PATCH",
            body=pick_by_keys(kwargs, "archived", "properties", "icon", "cover"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )


class UsersEndpoint(BaseRpcService):
    def list(self, **kwargs: Any) -> SyncAsync[Any]:
        """Return a paginated list of [Users](https://developers.notion.com/reference/user) for the workspace.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/get-users)*
        """  # noqa: E501
        return self.invoker.request(
            path="users",
            method="GET",
            query=pick_by_keys(kwargs, "start_cursor", "page_size"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )

    def retrieve(self, user_id: str, **kwargs: Any) -> SyncAsync[Any]:
        """Retrieve a [User](https://developers.notion.com/reference/user) using the ID specified.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/get-user)*
        """  # noqa: E501
        return self.invoker.request(
            path=f"users/{user_id}", method="GET", auth=kwargs.get("auth")
        )

    def me(self, **kwargs: Any) -> SyncAsync[Any]:
        """Retrieve the bot [User](https://developers.notion.com/reference/user) associated with the API token.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/get-self)*
        """  # noqa: E501
        return self.invoker.request(
            path="users/me", method="GET", auth=kwargs.get("auth")
        )


class SearchEndpoint(BaseRpcService):
    def __call__(self, **kwargs: Any) -> SyncAsync[Any]:
        """Search all pages and child pages that are shared with the integration.

        *[🔗 Endpoint documentation](https://developers.notion.com/reference/post-search)*
        """  # noqa: E501
        return self.invoker.request(
            path="search",
            method="POST",
            body=pick_by_keys(kwargs, "query", "sort", "filter", "start_cursor", "page_size"),
            auth=kwargs.get("auth"),base_url=self.base_url
        )
