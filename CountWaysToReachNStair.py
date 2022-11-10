
class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        MOD = 10**9 + 7
        
        mem = [1, 2]
        length = 2
        
        while length <= n:
            mem.append(mem[-1] + mem[-2])
            length += 1
            
        return mem[n-1] % MOD
        # code here