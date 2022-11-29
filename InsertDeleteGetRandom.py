import random

class RandomizedSet:

    def __init__(self):
        self.mem = set()
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.mem:
            return False

        self.mem.add(val)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.mem:
            self.mem.remove(val)
            self.lst.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()