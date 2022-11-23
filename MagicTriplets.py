#User function Template for python3

class Solution:
	def countTriplets(self, nums):
		# Code here
		ans = 0
		n = len(nums)
		for i in range(n):
		    l,r = 0,0
		    for j in range(i):
		        if nums[j] < nums[i]:
		            l += 1
		    for k in range(i+1,n):
		        if nums[k] > nums[i]:
		            r += 1
		    
		    ans += (r*l)
		    
        return ans