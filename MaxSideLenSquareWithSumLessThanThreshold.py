class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat:
            return 0

        ans = 0
        m = len(mat)
        n = len(mat[0])

        mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                mem[i][j] = mem[i-1][j] + mem[i][j-1] - mem[i-1][j-1] + mat[i-1][j-1]
                left = 1
                right = min(i,j)
                while left <= right:
                    mid = (left + right)//2
                    curr = mem[i][j] - mem[i-mid][j] - mem[i][j-mid] + mem[i-mid][j-mid]
                    if curr <= threshold:
                        ans = max(ans, mid)
                        left = mid + 1
                    else:
                        right = mid - 1

        return ans
