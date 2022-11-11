class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ans = float('inf')
        rows = len(heights)
        cols = len(heights[0])

        if rows <= 1 and cols <= 1:
            return 0

        def helper(diff):

            queue = deque([(0,0)])
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            
            while queue:
                x, y = queue.popleft()
                h = heights[x][y]
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=x+i<rows and 0<=y+j<cols:
                        if abs(h - heights[x+i][y+j]) <= diff and not visited[x+i][y+j]:
                            visited[x+i][y+j] = True
                            queue.append((x+i,y+j))

            return visited[-1][-1]

        left = 0
        right = 1000000

        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1

        return left
    
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         rows, cols = len(heights), len(heights[0])
#         pq = [(0,0,0)]

#         effort = [[float('inf') for j in range(cols)] for i in range(rows)]
#         effort[0][0] = 0

#         while pq:
#             diff, i, j = heapq.heappop(pq)
#             for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
#                 if 0<=i+di<rows and 0<=j+dj<cols:
#                     new_diff = max(diff, abs(heights[i][j] - heights[i+di][j+dj]))
#                     if effort[i+di][j+dj] > new_diff:
#                         effort[i+di][j+dj] = new_diff
#                         heapq.heappush(pq, (new_diff, i+di, j+dj))

#         return effort[-1][-1]
 