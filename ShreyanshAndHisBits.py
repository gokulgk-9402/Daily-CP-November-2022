class Solution:
    def count (self, N):
        # code here 
        
        def comb(n,r):
            if r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if mem[n][r] != -1:
                return mem[n][r]
                
            mem[n][r] = comb(n-1, r-1) + comb(n-1, r)
            return mem[n][r]
            
        mem = [[-1]*40 for _ in range(40)]
        ans = 0
        ones = 0
        bits = 0
        while N!= 0:
            if N&1:
                ans += comb(bits, ones+1)
                ones += 1
            bits += 1
            N = N>>1
        return ans