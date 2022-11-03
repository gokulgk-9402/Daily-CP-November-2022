class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = 0
        mem = Counter(words)
        flag = True
        for key in mem:
            if key[0] == key[1]:
                if mem[key]%2:
                    if flag:
                        count += mem[key]
                        flag = False
                    else:
                        count += mem[key]-1
                else:
                    count += mem[key]
            elif mem[key] != 0:
                if key[::-1] in mem and mem[key[::-1]] != 0:
                    val = min(mem[key], mem[key[::-1]])
                    count += 2*val
                    mem[key] -= val
                    mem[key[::-1]] -= val

        return 2*count