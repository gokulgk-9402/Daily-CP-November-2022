from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def distance(x1,y1,x2,y2):
            return pow((x1-x2)**2 + (y1-y2)**2, 0.5)

        n = len(bombs)
        graph = {i:[] for i in range(n)}

        def dfs(u):
            stack = [u]
            vis = set()

            while stack:
                u = stack.pop()
                if u in vis:
                    continue
                vis.add(u)
                for v in graph[u]:
                    stack.append(v)
            
            return len(vis)

        for i in range(n):
            for j in range(i+1,n):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]

                d = distance(x1,y1,x2,y2)
                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)

        ans = float('-inf')
        for bomb in graph:
            ans = max(ans, dfs(bomb))

        return ans
        
