from typing import List
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: x[0])
        start = [job[0] for job in jobs]
        end = [job[1] for job in jobs]
        p = [job[2] for job in jobs]
        
        mem = [0]*n
        mem[-1] = p[-1]
        for i in range(n-2, -1, -1):
            ind = bisect_left(start, end[i])
            mem[i] = max(p[i] + mem[ind] if ind < n else p[i], mem[i+1])
            
        return mem[0]
        

print(Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))