#User function Template for python3
from collections import Counter
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        mem = Counter(Arr)
        return sorted([key for key in mem if mem[key]%2], reverse=True)