#User function Template for python3
class Solution:
	def addBinary(self, A, B):
		# code here
		n1 = int(A, 2)
		n2 = int(B, 2)
		
		return bin(n1+n2)[2:]