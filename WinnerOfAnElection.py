#User function Template for python3
from collections import Counter
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        ctr = Counter(arr)
        # print(ctr)
        
        votes = 0
        winner = ""
        
        for key in ctr:
            if ctr[key] > votes:
                votes = ctr[key]
                winner = key
            elif ctr[key] == votes:
                if key < winner:
                    winner = key
                    
        return [winner, votes]