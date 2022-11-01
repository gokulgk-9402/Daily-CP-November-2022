#User function Template for python3
from bisect import bisect_right

class Solution:
    def median(self, matrix, R, C):
    	#code here 
    	minimum = float("inf")
    	maximum = float("-inf")
    	
    	for i in range(R):
    	    minimum = min(matrix[i][0], minimum)
    	    maximum = max(matrix[i][C-1], maximum)
    	    
    	req = (R*C + 1)//2
    	
    	while minimum < maximum:
    	    mid = (maximum + minimum) // 2
    	    pos = 0
    	    for i in range(R):
    	        pos += bisect_right(matrix[i], mid)
    	    if pos < req:
    	        minimum = mid + 1
    	    else:
    	        maximum = mid
    	        
    	return minimum