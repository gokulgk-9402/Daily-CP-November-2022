class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countneg = 0

        for num in nums:
            if num < 0:
                countneg += 1
            elif num==0:
                return 0

        if countneg%2:
            return -1
        
        return 1