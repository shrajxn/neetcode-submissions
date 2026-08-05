class MyHashMap:
    def __init__(self):
        self.hash1={}

    def put(self, key: int, value: int) -> None:
        self.hash1[key]=value
    def get(self, key: int) -> int:
        return self.hash1.get(key,-1)
    def remove(self, key: int) -> None:
        if key in self.hash1:
            del self.hash1[key]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)