#User function Template for python3
import math
class Solution:
	def baseEquiv(self, n, m):
		# code here
		high = 32
		low = 2
		
		def digits(num, base):
		    return int(math.log(num, base))
		
		while low <= high:
		    mid = (high + low)//2
		    
		    val = digits(n, mid) + 1
		    
		    if val == m:
		        return "Yes"
		       
		    elif val < m:
		        high = mid -1
		    
		    else:
		        low = mid + 1
		        
	    return "No"