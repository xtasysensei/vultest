#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import Modules
import json
import requests

__Name__ = "scancss"
__description__ = "scancss is a xss vulnariblity scanner tool."
__author__ = "Md. Nur habib"
__copyright__ = "Copyright 2022."
__license__ = "GNU v.20"
__version__ = "v1.0.1"
__email__ = "thenurhabib@gmail.com"


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
       ___          __  _      _  ____________
   /   |  ____  / /_(_)    | |/ / ___/ ___/
  / /| | / __ \/ __/ /_____|   /\__ \\__ \ 
 / ___ |/ / / / /_/ /_____/   |___/ /__/ / 
/_/  |_/_/ /_/\__/_/     /_/|_/____/____/     {Style.reset}{Style.red}{__version__}{Style.yellow}  
   Anti Xss scanner ======================================================
{Style.reset} \n\n"""
