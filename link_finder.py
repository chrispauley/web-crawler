from HTMLParser import HTMLParser
# from urlparse import urlparse
try:
    from urlparse import urlparse
except ImportError:
     from urllib.parse import urlparse

def urljoin(*args):
    return "/".join(map(lambda x: str(x).rstrip('/'), args))

# Responsible for
class LinkFinder(HTMLParser):

    def __init__(self, baseUrl, pageUrl):
        # super().__init__()
        HTMLParser.__init__(self)
        self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()

    def handle_starttag(self, tag, attrs):
        # print(tag)
        if tag == 'a':
            for (att, value) in attrs:
                if att == 'href':
                    url = urljoin(self.baseUrl, value)
                    self.links.add(url)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass


# finder = LinkFinder('http://mytest.com', 'index.html')
# finder.feed('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test</title></head>'
#             + '<body><h1>Parse Me!</h1><ul><li><a href="one.html"></a></li>'
#             + '<li><a href="two.html"></a></li></ul></body></html>')
