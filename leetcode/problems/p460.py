from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.d = {} # {key: [value, freq]}
        self.freq = {} # {freqkey: {key: None}}
        self.mn = 0

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        value, oldfreq = self.d[key]
        newfreq = oldfreq + 1
        self.d[key][1] = newfreq
        self.freq[oldfreq].pop(key)
        self.update_freq(key, newfreq)

        if oldfreq == self.mn and len(self.freq[oldfreq]) == 0:
            self.mn = oldfreq + 1
        
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            _ = self.get(key)
            self.d[key][0] = value
            return
        if len(self.d) == self.capacity:
            rm_key, _ = self.freq[self.mn].popitem(False)
            self.d.pop(rm_key)
        self.d[key] = [value, 1]
        self.update_freq(key, 1)
        self.mn = 1

    def update_freq(self, key, newfreq):
        if newfreq not in self.freq:
            self.freq[newfreq] = OrderedDict()

        self.freq[newfreq][key] = None
