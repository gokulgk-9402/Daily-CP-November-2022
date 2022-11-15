#User function Template for python3

class Solution:
    def getMaxandMinProduct(self, arr, n):
        # code here
        fib = [0,1]
        maximum = max(arr)
        
        while fib[-1] <= maximum:
            fib.append(fib[-1] + fib[-2])
            
        fib = set(fib)
        
        ans = []
        for ele in arr:
            if ele in fib:
                ans.append(ele)
                
        return ans