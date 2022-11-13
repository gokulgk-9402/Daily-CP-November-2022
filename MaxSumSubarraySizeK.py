#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        ans = 0
        left = 0
        for right in range(K):
            ans += Arr[right]
            right += 1
            
        curr = ans
        
        while left < N-K:
            curr += Arr[right]
            curr -= Arr[left]
            right += 1
            left += 1
            
            ans = max(ans, curr)
            
        return ans