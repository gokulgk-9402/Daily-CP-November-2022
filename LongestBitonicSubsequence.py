#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
		n = len(nums)
		lis = [1] * n
		lds = [1] * n
		
		for i in range(n):
		    for j in range(i):
		        if nums[i] > nums[j]:
		            lis[i] = max(lis[i], lis[j] + 1)
		            
	    for i in range(n-1, -1, -1):
		    for j in range(n-1, i, -1):
		        if nums[i] > nums[j]:
		            lds[i] = max(lds[i], lds[j] + 1)
        
        return max([lis[i]+lds[i]-1 for i in range(n)])