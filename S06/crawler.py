import re
import urllib.request


class WebPages:
    to_be_crawled = {}
    crawled_items = {}
    
    def __init__(self, url):
        if url in self.to_be_crawled.keys():
            self = self.to_be_crawled[url]
            
        elif url in self.crawled_items.keys():
            self = self.crawled_items[url]
            
        else:
            self.__url = url

    @property
    def url(self):
        return self.__url

    def __read_web_content(self):
        req = urllib.request.Request(self.__url)
        with urllib.request.urlopen(req) as response:
           return  response.read()


    def __get_links_str(self):
        txt = self.__read_web_content()
        res = re.findall(r'<a.*?href="(https?://.*?)"', str(txt))
        return res


    def grab(self):
        objs = map(WebPages, self.__get_links_str())

        return objs

    def __eq__(self, other):
        return self.url == other.url

    


wp = WebPages('http://www.python.org')
lst = wp.grab()
