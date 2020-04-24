import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.deque_ = collections.deque()
        self.deque_.append(-1)
        self.deque_.append(-1)
        self.dict_ = {}

    def get(self, key: int) -> int:
        if key in self.deque_:
            pass

    def put(self, key: int, value: int) -> None:
        pass


# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    cache = LRUCache(capacity=2)
    cache.put(1, 1);
    cache.put(2, 2);
    print(cache.get(1));       #  returns 1
    cache.put(3, 3);    #  evicts key 2
    print(cache.get(2));       #  returns -1 (not found)
    cache.put(4, 4);    #  evicts key 1
    print(cache.get(1));       #  returns -1 (not found)
    print(cache.get(3));       #  returns 3
    print(cache.get(4));       #  returns 4