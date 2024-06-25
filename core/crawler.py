from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse


class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    new_url = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [new_url]

    def get_links(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type') == 'text/html':
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            self.feed(html_string)
            return html_string, self.links
        else:
            return "", []


def spider(url, max_pages):
    links = []
    pages_to_visit = [url]
    number_visited = 0
    found_word = False
    while number_visited < max_pages and pages_to_visit != [] and not found_word:
        number_visited = number_visited + 1
        url = pages_to_visit[0]
        pages_to_visit = pages_to_visit[1:]
        try:
            parser = LinkParser()
            data, links = parser.get_links(url)
        except Exception as e:
            pass
        return links

#print(spider("http://vulnweb.com", 10))
