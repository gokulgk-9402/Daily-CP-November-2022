from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def valid(curr, next):
            diff = 0
            for i in range(8):
                if curr[i] != next[i]:
                    diff += 1
            
            return diff==1

        queue = [(start, 0)]
        visited = set()
        visited.add(start)

        while queue:
            curr, t = queue.pop(0)
            if curr == end:
                return t
            
            for string in bank:
                if valid(curr, string) and string not in visited:
                    queue.append((string, t+1))
                    visited.add(string)

        return -1