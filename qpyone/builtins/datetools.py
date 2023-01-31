import datetime

from datetime import date
from datetime import datetime
from datetime import timedelta


__all__ = ["get_date_by_timedelta", "current_tztime", "expand_datetime"]

from typing import Optional
from typing import Tuple


def tomorrow() -> datetime:
    """获取昨天的时间"""
    return datetime.now() + datetime.timedelta(days=1)


def yesterday() -> datetime:
    """获取昨天的时间"""
    return datetime.now() - datetime.timedelta(days=1)


def get_date_by_timedelta(days=0, from_date=date.today()):
    return from_date + timedelta(days=days)


def current_tztime() -> datetime:
    return datetime.now().astimezone()


def brief_datetime(dt: datetime) -> str:
    dtt = dt.astimezone() if dt.tzinfo is None else dt
    return dtt.isoformat()


def expand_datetime(dt_str: str) -> datetime:
    return datetime.fromisoformat(dt_str)


def datetime_to_str(value, fmt="%Y-%m-%d %H:%M:%S"):
    """时间类型转换为字符串。datetime to string.

    :type value: datetime
    :type fmt: str
    :rtype: str
    """
    return value.strftime(fmt)


def datetime_combine(
    start_date: datetime.date,
    end_date: datetime.date = None,
    delta_days: Optional[int] = None,
) -> Tuple[datetime, datetime]:
    """获取一段日期的起止时间。get start/end datetime from date.

    Examples::

        start, end = datetime_combine(datetime.date.today())
        yesterday, today = datetime_combine(datetime.date.today(), delta_days=-1)
        today, a_week_after = datetime_combine(datetime.date.today(), delta_days=7)
    """
    if end_date and delta_days is not None:
        raise ValueError("Can not specify end_date and delta_days at the same time")
    if delta_days is not None:
        start_date, end_date = start_date, start_date + datetime.timedelta(
            days=delta_days
        )
        if delta_days < 0:
            start_date, end_date = end_date, start_date
    end_date = end_date or start_date
    return (
        datetime.combine(start_date, datetime.time.min),
        datetime.combine(end_date, datetime.time.max),
    )
