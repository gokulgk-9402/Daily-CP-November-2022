class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.curr = 0
        self.length = len(encoding)

    def next(self, n: int) -> int:
        while self.curr < self.length and self.encoding[self.curr] < n:
            n -= self.encoding[self.curr]
            self.curr += 2
        
        if self.curr == self.length:
            return -1

        self.encoding[self.curr] -= n
        return self.encoding[self.curr + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)