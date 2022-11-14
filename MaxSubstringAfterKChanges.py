#User function Template for python3

class Solution:
	def characterReplacement(self, s, k):
		# Code here
		n = len(s)
		mem = {chr(i): 0 for i in range(65, 91)}
		start = 0
		max_count = 0
		ans = 0
		
		for end in range(n):
		    mem[s[end]] += 1
		    max_count = max(max_count, mem[s[end]])
		    while end-start+1-max_count > k:
		        mem[s[start]] -= 1
		        start += 1
		    ans = max(ans, end-start + 1)
		    
        return ans