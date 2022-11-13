#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        for i in range(N):
            if not arr[i]:
                arr[i] = -1
                
        curr = 0
        ans = 0
        mem = {0:-1}
        
        for i in range(N):
            curr += arr[i]
            if curr in mem:
                ans = max(ans, i-mem[curr])
            else:
                mem[curr] = i
                
        return ans