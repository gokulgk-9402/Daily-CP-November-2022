class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        queue = deque([[entrance[0], entrance[1], 0]])

        while queue:
            r,c,d = queue.popleft()
            if visited[r][c]:
                continue
            visited[r][c] = True

            if r!=entrance[0] or c!=entrance[1]:
                if r == 0 or r == rows-1 or c == 0 or c == cols - 1:
                    # print(r,c,rows,cols)
                    return d

            for dr,dc in [(0,1), (1, 0), (0,-1), (-1,0)]:
                if 0<=r+dr<rows and 0<=c+dc<cols:
                    if maze[r+dr][c+dc] == '.':
                        queue.append([r+dr, c+dc, d+1])

        return -1
