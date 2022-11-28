class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        ans = 0
        mem = [defaultdict(int) for _ in range(length)]

        for i in range(length):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += mem[j][diff]
                mem[i][diff] += mem[j][diff] + 1

        return ans