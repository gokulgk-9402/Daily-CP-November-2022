#User function Template for python3
class Solution:
    def isSumOfTwo (self, N):
        # code here 
        
        def isprime(num):
            if num == 1:
                return False
            
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
                    
            return True
            
        if N < 4:
            return "No"
            
        if N%2 == 0:
            return "Yes"
            
        if isprime(N-2):
            return "Yes"
        
        return "No"