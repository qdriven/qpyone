#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Dict, Optional

from pydantic import BaseModel


class ExpectedResponse(BaseModel):
    status_code: int = 200
    values: Optional[Dict]
