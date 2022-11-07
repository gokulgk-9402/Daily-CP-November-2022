from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        queue = deque([(start, 0)])
        visited = set()
        
        while queue:
            for _ in range(len(queue)):
                x, t = queue.popleft()
                if x == goal:
                    return t
                
                if x < 0 or x > 1000:
                    continue

                if x in visited:
                    continue

                visited.add(x)

                for num in nums:
                    queue.append((x+num, t+1))
                    queue.append((x-num, t+1))
                    queue.append((x^num, t+1))

        return -1
