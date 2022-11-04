from typing import Optional

import datetime

from pydantic import BaseModel


class UserHistory(BaseModel):

    runid: float | None
    job_id: float | None
    id: str
    user: str
    status: str
    event_time: datetime.datetime = datetime.datetime.now()
    comment: str = "none"
