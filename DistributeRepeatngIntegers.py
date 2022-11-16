from typing import List
from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:

        mem = Counter(nums)
        frequencies = sorted(list(mem.values()), reverse=True)

        n = len(quantity)
        frequencies = frequencies[:n]
        length = len(frequencies)

        subsums = [0] * (1<<n)
        for mask in range(1<<n):
            for i in range(n):
                if mask & (1<<i):
                    subsums[mask] += quantity[i]

        q = {0}
        for i in range(length):
            q_next = set()
            for mask in q:
                not_mask = ((1<<n) - 1) ^ mask
                submask = not_mask
                while submask:
                    if subsums[submask] <= frequencies[i]:
                        next_mask = mask | submask
                        if next_mask == (1<<n) -1 :
                            return True
                        q_next.add(next_mask)
                    submask = (submask - 1) & not_mask
            q = q_next
        
        return False