#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import Modules
import requests
from core.core import *
from lib.Log import *
from bs4 import BeautifulSoup
from lib.helper import *
from urllib.parse import urljoin
from multiprocessing import Process


# Crawler Class.
class Crawler:
    visited = []

    @classmethod
    def get_links(cls, base, proxy, headers, cookie):

        lst = []

        conn = session(proxy, headers, cookie)
        text = conn.get(base).text
        isi = BeautifulSoup(text, "html.parser")

        for obj in isi.find_all("a", href=True):
            url = obj["href"]

            if url.startswith("http://") or url.startswith("https://"):
                continue

            elif url.startswith("mailto:") or url.startswith("javascript:"):
                continue

            elif urljoin(base, url) in cls.visited:
                continue

            else:
                lst.append(urljoin(base, url))
                cls.visited.append(urljoin(base, url))

        return lst

    @classmethod
    def crawl(cls, base, depth, proxy, headers, level, method, cookie):

        urls = cls.get_links(base, proxy, headers, cookie)

        for url in urls:

            p = Process(target=Core.main, args=(
                url, proxy, headers, level, cookie, method))
            p.start()
            p.join()
            if depth != 0:
                cls.crawl(url, depth - 1, base, proxy, level, method, cookie)

            else:
                break
