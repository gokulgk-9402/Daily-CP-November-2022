class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        def helper(n):
            for i in range(rows):
                n2 = n + grid[i][n]
                if n2 < 0 or n2 >= cols or grid[i][n] != grid[i][n2]:
                    return -1
                n = n2
            return n

        return [helper(x) for x in range(cols)]