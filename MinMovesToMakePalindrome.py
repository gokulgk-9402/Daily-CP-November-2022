from math import ceil

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:

        ans = 0
        n = len(s)

        req = n-1
        for i in range(ceil(n/2)):
            for j in range(req, i-1, -1):
                if j == i:
                    ans += n//2 - i
                elif s[i] == s[j]:
                    s = s[:j] + s[j+1:req+1] + s[j] + s[req+1:]
                    ans += req - j
                    req -= 1
                    break

        return ans