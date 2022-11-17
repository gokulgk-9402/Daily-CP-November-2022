#User function Template for python3
class Solution:


	def countSubarray(self,arr, n, k):
	    # code here
	    
	    t = 0
	    i = 0
	    while i < n:
	        if arr[i] <= k:
	            count = 0
	            while i<n and arr[i] <= k:
	                i += 1
	                count +=1
	            t += (count * (count + 1))//2
	        else:
	            i += 1

        return (n*(n+1))//2 - t