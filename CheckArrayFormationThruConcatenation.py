from typing import List
from collections import defaultdict

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mem = defaultdict(list)
        for piece in pieces:
            mem[piece[0]] = piece
        
        ans = []
        for ele in arr:
            ans += mem[ele]

        return ans == arr