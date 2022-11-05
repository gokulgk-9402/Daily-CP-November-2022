class Solution:
    def reverseVowels(self, s: str) -> str:
        mem = []
        count = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        for ch in s:
            if ch in vowels:
                mem.append(ch)
                count += 1
        
        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = mem[count-1]
                count -= 1

        return "".join(s)