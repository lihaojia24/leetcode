class MyHashMap:

    def __init__(self):
        self.m = [-1] * 1_000_000

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        return self.m[key]

    def remove(self, key: int) -> None:
        self.m[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)