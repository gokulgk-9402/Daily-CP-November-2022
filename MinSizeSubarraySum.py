class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        curr = 0
        left = 0

        length = len(nums)

        ans = float('inf')

        for i in range(length):
            curr += nums[i]

            while curr >= target:
                ans = min(ans, i+1-left)
                curr -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0

        return ans
