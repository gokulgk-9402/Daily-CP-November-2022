#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n = len(matrix)
		
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            if matrix[i][k] > 0 and matrix[k][j] > 0:
    		            val = matrix[i][k] + matrix[k][j]
    		            if (matrix[i][j] == -1 or matrix[i][j] > val):
    		                matrix[i][j] = val
		                
		return matrix