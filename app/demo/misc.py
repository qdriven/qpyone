#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def get_public_ip():
    ip = requests.get("https://ifconfig.info/ip", verify=False).text.strip()
    return {"ip": ip}

def handle():
    return {"message": "Hello World"}

