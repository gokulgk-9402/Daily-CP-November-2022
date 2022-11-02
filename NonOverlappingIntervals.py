class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        length = len(intervals)

        if length < 2:
            return 0

        curr = intervals[0][1]
        ans = 0
        for i in range(1, length):
            if curr > intervals[i][0]:
                ans += 1
                curr = min(curr, intervals[i][1])
            else:
                curr = intervals[i][1]

        return ans