#User function Template for python3

class Solution:

	def findSubarray(self,a, n):
    	# code here
    	arrays = [[]]
    	
    	for ele in a:
    	    if ele < 0:
    	        arrays.append([])
    	        continue
    	    arrays[-1].append(ele)
        
        ans = max(arrays, key= lambda x: sum(x))
        if not ans:
            return [-1]
            
        return ans