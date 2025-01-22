class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.current = 0

    def get_next_proxy(self):
        proxy = self.proxies[self.current]
        self.current = (self.current + 1) % len(self.proxies)
        return proxy
