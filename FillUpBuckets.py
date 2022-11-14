#User function Template for python3

class Solution:
	def totalWays(self, n, capacity):
		# code here
		capacity.sort()
		ans = 1
		MOD = 10**9 + 7
		
		flag = False
	    for i in range(n-1,-1,-1):
	        if capacity[i] < i:
	            flag = True
	            break
	        else:
	            ans = ans * (capacity[i]-i)
	            ans %= MOD
	    if flag:
	        return 0
		    
	    return ans