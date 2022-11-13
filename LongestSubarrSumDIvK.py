#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		
		curr = 0
		mem = {0:-1}
		ans = 0
		
		for i in range(n):
		    curr += arr[i]
		    if curr%K in mem:
		        ans = max(ans, i-mem[curr%K])
		    else:
		        mem[curr%K] = i
		        
	    return ans