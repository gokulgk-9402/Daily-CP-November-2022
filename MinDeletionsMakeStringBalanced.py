class Solution:
    def minimumDeletions(self, s: str) -> int:

        pre_b = [0]
        suf_a = [0]

        length = len(s)

        for i in range(1, length):
            if s[i-1] == 'b':
                pre_b.append(pre_b[-1] + 1)
            else:
                pre_b.append(pre_b[-1])

            if s[-i] == 'a':
                suf_a.append(suf_a[-1] + 1)
            else:
                suf_a.append(suf_a[-1])

        minimum = float('inf')

        for i in range(length):
            minimum = min(minimum, pre_b[i] + suf_a[-i-1])

        return minimum