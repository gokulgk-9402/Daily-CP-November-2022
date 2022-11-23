#User function Template for python3
class Solution:
    def maxSumLCM (self, n):
        # code here 
        ans = 0
        i = 1
        while i <= n**0.5:
            if n%i==0:
                ans += i
                if n != i**2:
                    ans += n//i
            i += 1
        
        return ans