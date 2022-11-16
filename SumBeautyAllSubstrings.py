#User function Template for python3
from collections import defaultdict

class Solution:
    def beautySum(self, s):
        # Code here
        n = len(s)
        ans = 0
        
        for i in range(n):
            mem = defaultdict(int)
            maximum = 0
            for j in range(i,n):
                mem[s[j]] += 1
                maximum = max(maximum, mem[s[j]])
                minimum = min(mem.values())
                ans += (maximum - minimum)
                
        return ans