class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==0:
            return []

        nums.sort()
        mem = []
        target = [-1 for _ in range(n)]

        for i in range(n):
            mem.append(1)
            j = 0
            while j < i:
                if nums[i]%nums[j] == 0:
                    if mem[i] < mem[j] + 1:
                        mem[i] = mem[j] + 1
                        target[i] = j

                j += 1

        temp = max(mem)
        ind = mem.index(temp)
        ans = [nums[ind]]
        temp = target[ind]
        while temp != -1:
            ans.append(nums[temp])
            temp = target[temp]
        return ans