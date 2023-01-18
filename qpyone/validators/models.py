#!/usr/bin/env python

from pydantic import BaseModel


class ExpectedResponse(BaseModel):
    status_code: int = 200
    values: dict | None
