#!/usr/bin/env python
"""
render by jinja2 template engine
"""
import json

from jinja2 import Template
from qpyone.builtins.datetools import get_date_by_timedelta
from qpyone.builtins.randomtools import faker
from qpyone.builtins.randomtools import random_str


render_func = {
    "get_date_by_timedelta": get_date_by_timedelta,
    "faker": faker,
    "random_str": random_str,
}


def render_template(temp_str, context):
    template = Template(temp_str)
    template.globals.update(render_func)
    return template.render(context)


def render_without_context(temp_str, default_return_str="N"):
    if temp_str is None:
        return default_return_str
    # print(temp_str)
    return render_template(temp_str, {})


def render_to_dict(dict_or_json, context):
    template = Template(json.dumps(dict_or_json))
    template.globals.update(render_func)
    filled_str = template.render(context)
    return json.loads(filled_str, encoding="utf-8")
