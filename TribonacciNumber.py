class Solution:
    def tribonacci(self, n: int) -> int:
        mem = [0, 1, 1]
        length = 3

        while length<=n+1:
            mem.append(mem[-1] + mem[-2] + mem[-3])
            length += 1

        return mem[n]