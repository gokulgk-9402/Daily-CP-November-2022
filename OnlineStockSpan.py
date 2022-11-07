class StockSpanner:

    def __init__(self):
        self.mem = []
        
    def next(self, price: int) -> int:
        ans = 1
        while self.mem and self.mem[-1][0] <= price:
            ans += self.mem.pop()[1]

        self.mem.append([price, ans])
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)