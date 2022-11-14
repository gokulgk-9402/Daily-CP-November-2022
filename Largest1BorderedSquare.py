class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        top = [a[:] for a in grid]
        left = [a[:] for a in grid]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    if i:
                        top[i][j] = top[i-1][j] + 1
                    if j:
                        left[i][j] = left[i][j-1] + 1

        for r in range(min(rows, cols), 0, -1):
            for i in range(rows-r+1):
                for j in range(cols-r+1):
                    if min(top[i+r-1][j], top[i+r-1][j+r-1], left[i][j+r-1], left[i+r-1][j+r-1]) >= r:
                        return r*r

        return 0