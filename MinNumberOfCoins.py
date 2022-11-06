#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        ans = []
        
        ptr = 9
        while N:
            if denominations[ptr] > N:
                ptr -= 1
            else:
                ans.append(denominations[ptr])
                N -= denominations[ptr]
                
        return ans