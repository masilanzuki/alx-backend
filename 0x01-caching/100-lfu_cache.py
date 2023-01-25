from base_caching import BaseCaching
from collections import Counter
from collections import OrderedDict


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = Counter()
        self.order = OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            min_freq_keys = [key for key, freq in self.frequency.items() if freq == min_freq]
            lru_key = min(min_freq_keys, key=lambda x: list(self.order.keys()).index(x))
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            del self.order[lru_key]
            print("DISCARD: {}\n".format(lru_key))
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.order[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
