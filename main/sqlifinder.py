import requests
import re
import argparse
import os
import sys
import time
import requests
import string

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from lib.colors import *
from core import requester
from core import extractor
from core import crawler
from urllib.parse import unquote
from tqdm import tqdm

start_time = time.time()


def clear():
    if 'linux' in sys.platform:
        os.system('clear')
    elif 'darwin' in sys.platform:
        os.system('clear')
    else:
        os.system('cls')


def banner():
    ban = '''
      '''

    print(ban)


def concatenate_list_data(list, result):
    for element in list:
        result = result + "\n" + str(element)
    return result


def log_vulnerability(final_url, payload):
    with open("vulnerabilities/vulnerabilities.txt", "a") as f:
        f.write(f"---------------[SQLi found!]-----------------\n")
        f.write(f"[sql-injection]\n")
        f.write(f"Payload: {payload}\n")
        f.write(f"URL: {final_url}\n\n")


def main():
    parser = argparse.ArgumentParser(description='sqliscanner')
    parser.add_argument('-d', '--domain', help='Domain name of the target [ex. example.com]', required=True)
    parser.add_argument('-s', '--subs', help='Set false or true [ex: --subs False]', default=False)
    args = parser.parse_args()

    if args.subs:
        url = f"http://web.archive.org/cdx/search/cdx?url=*.{args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    else:
        url = f"http://web.archive.org/cdx/search/cdx?url={args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"

    '''for i in tqdm (range (100), desc="Starting..."): 
        time.sleep(0.01)'''

    response = requester.connector(url)
    crawled_urls = crawler.spider(f"http://{args.domain}", 10)
    response = concatenate_list_data(crawled_urls, response)
    if not response:
        return
    response = unquote(response)
    print(" ")
    print(f"{bold}{blue} SQL finder{end}{cyan}")
    print(f"************")
    print(f"""{yellow}[INF]{end} {green}Scanning sql injection for{end} {blue}{args.domain}{end}""")

    exclude = ['woff', 'js', 'ttf', 'otf', 'eot', 'svg', 'png', 'jpg']
    final_uris = extractor.param_extract(response, "high", exclude, "")

    file = open('payload/payloads.txt', 'r')
    payloads = file.read().splitlines()

    vulnerable_urls = []

    for uri in final_uris:
        for payload in payloads:
            final_url = uri + payload

            try:
                req = requests.get("{}".format(final_url))
                res = req.text
                print(f"""{yellow}[*] Testing {end}{blue}{uri}{end}{red}{payload}{end}""")
                if 'SQL' in res or 'sql' in res or 'Sql' in res:
                    print(f"""
{red}#{yellow}------------------------------------------------------------------------------------------{red}#{end}
{red}{purple}[sql-injection] {end}
Payload: {red}{payload}{end}  
URL: {red}{final_url}{end}
{red}#{yellow}------------------------------------------------------------------------------------------{red}#{end}
                        """)
                    log_vulnerability(final_url, payload)
                    break
            except KeyboardInterrupt:
                print(f"""
                    ************************
                    {yellow}SQLi Scan cancelled {end}
                    ************************
                    """)
                sys.exit()
            except:
                pass


if __name__ == "__main__":
    main()
