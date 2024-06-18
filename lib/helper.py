#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import Modules
import json
import requests

# Style class
class Style:
    reset = '\033[0m'
    bold = '\033[01m'
    underline = '\033[04m'
    red = '\033[31m'
    blue = '\033[34m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    yellow = '\033[93m'


agent = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
line = "—————————————————"


def session(proxies, headers, cookie):
    requestVariable = requests.Session()
    requestVariable.proxies = proxies
    requestVariable.headers = headers
    requestVariable.cookies.update(json.loads(cookie))
    return requestVariable


logo = f"""{Style.bold}{Style.yellow}
   Anti Xss scanner ======================================================
{Style.reset} \n\n"""
