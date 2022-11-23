class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high - low)//2
        if low%2 or high%2:
            return ans + 1
        
        return ans