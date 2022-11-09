#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		total = sum(arr)
		mem = [[-1 for _ in range(total+1)] for _ in range(n)]
		
		def helper(pos, s1, s2):
		    if pos < 0:
		        return abs(s1-s2)
		        
		    if mem[pos][s1] != -1:
		        return mem[pos][s1]
		    
		    v1 = helper(pos-1, s1+arr[pos], s2)
		    v2 = helper(pos-1, s1, s2+arr[pos])
		    
		    mem[pos][s1] = min(v1, v2)
		    
		    return mem[pos][s1]
		    
	    return helper(n-1, 0, 0)