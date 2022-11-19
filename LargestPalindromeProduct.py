class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        num = 10**n
        MOD = 1337

        for val in range(2, num):
            left = num - val
            right = int(str(left)[::-1])

            disc = val**2 - 4*right

            if disc >= 0:
                r1 = (val + disc**0.5)/2
                r2 = (val - disc**0.5)/2

                if r1 == int(r1) or r2 == int(r2):
                    return (num*left + right)%MOD