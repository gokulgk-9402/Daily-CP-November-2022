class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mem = {}

        for i, (s,e) in enumerate(intervals):
            mem[s] = i

        starts = sorted(list(mem.keys()))

        ans = []

        for s, e in intervals:
            if e in mem:
                ans.append(mem[e])

            else:
                ind = bisect.bisect_right(starts, e)
                if ind == len(starts):
                    ans.append(-1)
                else:
                    ans.append(mem[starts[ind]])

        return ans