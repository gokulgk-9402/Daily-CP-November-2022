from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        mem = {}
        def helper(start, end):
            ans = float('inf')
            if end-start < 2:
                return 0

            if (start,end) in mem:
                return mem[(start, end)]

            for i in range(start+1, end):
                ans = min(ans, helper(start, i) + helper(i,end) + values[i]*values[start]*values[end])
                mem[(start,end)] = ans
            
            return ans
        
        return helper(0, len(values)-1)