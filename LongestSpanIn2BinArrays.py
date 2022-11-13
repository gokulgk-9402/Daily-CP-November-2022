#User function template for Python

class Solution:
	def longestCommonSum(self, arr1, arr2, n): 
		# code here 
        temp = [arr1[i] - arr2[i] for i in range(n)]
        mem = {0:-1}
        curr = 0
        ans = 0
        
        for i in range(n):
            curr += temp[i]
            if curr in mem:
                ans = max(ans, i-mem[curr])
            else:
                mem[curr] = i
                
        return ans