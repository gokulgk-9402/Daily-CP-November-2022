#User function Template for python3

class Solution:
    def lcmTriplets(self,N):
        #code here
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N%2:
            return (N-2)*(N-1)*N
        elif N%3:   
            return (N-3)*(N-1)*(N)
        else:
            return (N-1)*(N-2)*(N-3)