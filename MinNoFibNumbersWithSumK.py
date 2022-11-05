class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        mem = [1, 1]
        while mem[-1] <= k:
            mem.append(mem[-1] + mem[-2])

        pos = len(mem) - 1
        ans = 0

        while k:
            while mem[pos] > k:
                pos -= 1
            
            k -= mem[pos]
            ans += 1

        return ans