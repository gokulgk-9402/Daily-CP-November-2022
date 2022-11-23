class Solution:
    def numSquares(self, n: int) -> int:
        
        mem = [float('inf') for _ in range(n+1)]
        mem[1] = 1
        perfect = [1]

        for i in range(2, n+1):
            if i**0.5 - int(i**0.5) == 0:
                mem[i] = 1
                perfect.append(i)
            else:
                for j in perfect:
                    mem[i] = min(mem[i], mem[i-j] + 1)
        
        return mem[n]