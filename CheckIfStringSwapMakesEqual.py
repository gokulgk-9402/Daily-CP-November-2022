class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False

        mis = 0
        chars = []

        for i in range(n):
            if s1[i] != s2[i]:
                if mis == 2:
                    return False
                
                chars.append(s1[i])
                chars.append(s2[i])
                mis += 1

        if mis == 0:
            return True
            
        if mis != 2:
            return False 

        if chars[0] == chars[-1] and chars[1] == chars[-2]:
            return True

        return False