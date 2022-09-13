#!/usr/bin/env python
from typing import Dict
from typing import Optional

from pydantic import BaseModel


class ExpectedResponse(BaseModel):
    status_code: int = 200
    values: dict | None
