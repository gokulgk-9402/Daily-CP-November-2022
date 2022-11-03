#User function Template for python3


class Solution:

	def removals(self,arr, n, k):
		# code here
		arr.sort()
		
		ans = float('inf')
		last = 0
		
		for end in range(n-1,-1,-1):
		    start = 0
		    while arr[end] - arr[start] > k:
		        start += 1
		    ans = min(ans, start+last)
		    last += 1
		        
		return ans