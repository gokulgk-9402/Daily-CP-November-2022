class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        
        m, n = len(grid), len(grid[0])
        A = [[0] * (n + 1) for _ in range(m + 1)]
        good = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                A[i + 1][j + 1] = A[i + 1][j] + A[i][j + 1] - A[i][j] + (1 - grid[i][j])
                if i + 1 >= stampHeight and j + 1 >= stampWidth:
                    x, y = i + 1 - stampHeight, j + 1 -stampWidth
                    if A[i + 1][j + 1] - A[x][j + 1] - A[i + 1][y] + A[x][y] == stampWidth * stampHeight:
                        good[i][j] += 1

        B = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + good[i][j]

        for i in range(m):
            for j in range(n):
                x, y = min(i + stampHeight, m), min(j + stampWidth, n)
                if grid[i][j] == 0 and B[x][y] - B[i][y] - B[x][j] + B[i][j] == 0:
                    return False
        return True