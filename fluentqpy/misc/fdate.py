#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import date, timedelta


def get_date_by_timedelta(days=0, from_date=date.today()):
    return from_date + timedelta(days=days)
