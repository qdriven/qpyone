#!/usr/bin/env python
from datetime import date
from datetime import timedelta


def get_date_by_timedelta(days=0, from_date=date.today()):
    return from_date + timedelta(days=days)
