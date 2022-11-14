#User function Template for python3
class Solution:
    def numberOfSubsequences (self,S,W):
        # code here 
        S = list(S)
        W = list(W)
        
        ans = 0
        
        while True:
            i,j = 0,0
            flag = False
            
            while i < len(S):
                if S[i] == W[j]:
                    S[i] = '*'
                    j += 1
                    if j == len(W):
                        ans += 1
                        flag = True
                        break
                    
                i += 1
                
            if not flag:
                break
                
        return ans
