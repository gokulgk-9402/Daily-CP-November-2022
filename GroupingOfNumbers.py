#User function Template for python3
from collections import defaultdict

class Solution:
    def maxGroupSize(self, arr, N, K):
        # code here 
        
        vis = [0] * K
        
        ans = 0
        
        for ele in arr:
            vis[ele%K] += 1
            
        for i in range(1, K//2):
            ans += max(vis[i], vis[-i])
            
        if vis[0]:
            ans += 1
            
        if K%2 == 0:
            if vis[K//2]:
                ans += 1
        else:
            ans += max(vis[K//2], vis[K//2+1])
            
        return ans