from datetime import date
from datetime import datetime
from datetime import timedelta


def get_date_by_timedelta(days=0, from_date=date.today()):
    return from_date + timedelta(days=days)


def current_tztime() -> datetime:
    return datetime.now().astimezone()


def brief_datetime(dt: datetime) -> str:
    dtt = dt.astimezone() if dt.tzinfo is None else dt
    return dtt.isoformat()


def expand_datetime(dt_str: str) -> datetime:
    return datetime.fromisoformat(dt_str)
