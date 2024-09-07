import requests
from core.core import *
from lib.Log import *
from bs4 import BeautifulSoup
from lib.helper import *
from urllib.parse import urljoin
from multiprocessing import Process, Queue
import sys

class Crawler:
    visited = []

    @classmethod
    def get_links(cls, base, proxy, headers, cookie):
        lst = []

        try:
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

        except requests.RequestException as e:
            Log.error(f"Error fetching links from {base}: {e}")

        return lst

    @classmethod
    def crawl(cls, base, depth, proxy, headers, level, method, cookie):
        urls = cls.get_links(base, proxy, headers, cookie)

        for url in urls:
            try:
                p = Process(target=Core.main, args=(
                    url, proxy, headers, level, cookie, method))
                p.start()
                p.join()

                if depth != 0:
                    cls.crawl(url, depth - 1, proxy, headers, level, method, cookie)

                else:
                    break

            except KeyboardInterrupt:
                print("\n************************")
                print("Crawling cancelled")
                print("************************")

                # Terminate the process if it's still running
                if p.is_alive():
                    p.terminate()
                    p.join()

                sys.exit(0)

            except Exception as e:
                Log.error(f"Error in crawling {url}: {e}")
