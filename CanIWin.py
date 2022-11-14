class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if desiredTotal == 0:
            return True

        max_sum = maxChoosableInteger*(maxChoosableInteger+1)
        max_sum //= 2
    
        if desiredTotal > max_sum:
            return False

        mem = {}

        def helper(mask, total):
            if mask >= 2**(total-1):
                return True
            if mask in mem:
                return mem[mask]

            for i in range(maxChoosableInteger):
                if mask & (1<<i):
                    newmask = mask & ~(1<<i)
                    if not helper(newmask, total-i-1):
                        mem[mask] = True
                        return True

            mem[mask] = False
            return False

        return helper(2**maxChoosableInteger-1, desiredTotal)