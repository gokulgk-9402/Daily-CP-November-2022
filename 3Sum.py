class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        if len(nums) < 3:
            return []

        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if i>=1 and num==nums[i-1]:
                continue
            mem = {}
            for x in nums[i+1:]:
                if x not in mem:
                    mem[-num-x] = 1
                else:
                    ans.add((num, -num-x, x))
        
        return [list(x) for x in ans]

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = set()
#         length = len(nums)
        
#         for i in range(length):
#             map = defaultdict(list)
#             s = -nums[i]
#             for j in range(i+1, length):
#                 if s-nums[j] in map:
#                     for ele in map[s-nums[j]]:
#                         ans.add(tuple(sorted([nums[i], s-nums[j], nums[j]])))
                
#                 map[nums[j]].append(j)

#         return [list(x) for x in ans]