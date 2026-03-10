from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.key_to_freq = dict()
        self.freq_to_keys = dict()
        self.capacity = capacity
        self.min_freq = 0


    def increment_frequency(self, key: int, value: int):
        key_freq = self.key_to_freq[key]
        del self.freq_to_keys[key_freq][key]

        if len(self.freq_to_keys[key_freq]) == 0:
            del self.freq_to_keys[key_freq]
        
        key_freq += 1
        self.key_to_freq[key] += 1

        if key_freq in self.freq_to_keys:
            self.freq_to_keys[key_freq][key] = value
        else:
            self.freq_to_keys[key_freq] = OrderedDict()
            self.freq_to_keys[key_freq][key] = value
        
        if self.min_freq == key_freq-1 and (key_freq-1) not in self.freq_to_keys:
            self.min_freq = key_freq

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        else:
            freq = self.key_to_freq[key]
            value = self.freq_to_keys[freq][key]
            self.increment_frequency(key, value)
        
        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_freq:
            self.increment_frequency(key, value)
        else:
            # Can move this to init and change put and get to simple lambdas to save some time.
            if self.capacity == 0:
                return
            
            if self.capacity == len(self.key_to_freq):
                if len(self.freq_to_keys[self.min_freq]) == 1:
                    del_key = list(self.freq_to_keys[self.min_freq].keys())[0]
                    del self.freq_to_keys[self.min_freq]
                    del self.key_to_freq[del_key]
                else:
                    # Select least recently used node from the node with the least frequently used keys.
                    del_key = self.freq_to_keys[self.min_freq].popitem(last=False)[0]
                    del self.key_to_freq[del_key]
            
            self.key_to_freq[key] = 1
            if 1 not in self.freq_to_keys:
                self.freq_to_keys[1] = OrderedDict()
            self.freq_to_keys[1][key] = value
            self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    actions = ["LFUCache","put","put","get","put","put","get"]
    values = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    cache = None
    for ii in range(len(actions)):
        action = actions[ii]
        value = values[ii]

        print(action + " " + str(value))

        if action == "LFUCache":
            cache = LFUCache(value[0])
        elif action == "put":
            cache.put(value[0], value[1])
        else:
            print(cache.get(value[0]))
        
        print(cache.key_to_freq.keys())
        print("")
