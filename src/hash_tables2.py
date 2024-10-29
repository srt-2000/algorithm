class CashTest:

    def __init__(self):
        self.data = None
        self.cache = {}

    def get_cache(self, url_name, page):
        if self.cache.get(url_name):
            print("It's a cache information")
            return self.cache[url_name]
        else:
            self.data = page.get(url_name)
            self.cache[url_name] = self.data
            print("It's a server side response")
            return self.data
