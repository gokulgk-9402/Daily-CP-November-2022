from collections import Counter
#User function Template for python3
class Solution:
    def oddEven(ob, S):
        # code here 
        
        X = 0
        Y = 0
        
        mem = Counter(S)
        
        for ch in mem:
            if ord(ch)%2:
                if mem[ch]%2:
                    X += 1
            else:
                if mem[ch]%2 == 0:
                    Y += 1
                    
        if (X+Y)%2:
            return "ODD"
            
        return "EVEN"