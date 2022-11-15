#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        #code here
        
        def ispossible(val):
            
            i = 0
            curr = 0
            count = 1
            while i < len(arr):
                curr += arr[i]
                
                if curr > val:
                    count += 1
                    curr = arr[i]
                    
                i += 1
                
            return count <= k
            
        low = max(arr)
        high = sum(arr)
        time = high
        while low < high:
            mid = (low + high)//2
            if ispossible(mid):
                time = min(time, mid)
                high = mid
                
            else:
                low = mid + 1
                
        return time