#User function Template for python3
from collections import deque

class Solution:
    def jumpingNums(self, X):
        # code here 
        ans = 0
        
        def bfs(num):
            nonlocal ans
            queue = deque([num])
            while queue:
                num = queue.popleft()
                if num <= X:
                    ans = max(ans, num)
                    last = num % 10
                    if last != 9:
                        queue.append(num*10 + last + 1)
                    if last != 0:
                        queue.append(num*10 + last - 1)
        
        for i in range(1, 10):
            if i <= X:
                bfs(i)
                
        return ans