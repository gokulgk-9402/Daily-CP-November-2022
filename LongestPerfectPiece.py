#User function Template for python3
from sortedcontainers import SortedList

class Solution:
    def longestPerfectPiece(self, arr, N):
        # code here 
        
        mem = SortedList()
        ans = 0
        
        i,j = 0,0
        
        while i < N:
            mem.add(arr[i])
            while mem[-1] - mem[0] > 1:
                mem.remove(arr[j])
                j += 1
            ans = max(ans, len(mem))
            i += 1
        return ans