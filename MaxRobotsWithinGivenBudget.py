from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        curr = 0
        i = 0
        length = len(chargeTimes)
        mem = SortedList()
        ans = 0
        for j in range(length):
            curr += runningCosts[j]
            mem.add(chargeTimes[j])
            
            tc = mem[-1] + (j-i+1)*curr

            if tc > budget:
                mem.remove(chargeTimes[i])
                curr -= runningCosts[i]
                i += 1
            else:
                ans = max(j-i+1, ans)

        return ans