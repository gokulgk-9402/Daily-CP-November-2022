#User function Template for python3

class Solution:
	def UniquePartitions(self, n):
		# Code here
		
		mem = [0] * n
		k = 0
		mem[k] = n
		ans = []
		
		while True:
		    ans.append(mem[:k+1])
		    rem = 0
		    while k >= 0 and mem[k] == 1:
		        rem += mem[k]
		        k -= 1
		        
            if k < 0:
                return ans
            
            mem[k] -= 1
            rem += 1
            
            while rem > mem[k]:
                mem[k+1] = mem[k]
                rem -= mem[k]
                k += 1
                
            mem[k+1] = rem
            k += 1