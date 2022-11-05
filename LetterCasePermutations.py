class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        ans = []
        s = list(s)

        positions = []
        count = 0

        for i in range(len(s)):
            if s[i].isalpha():
                positions.append(i)
                count += 1

        def recursion(string, pos):
            nonlocal count

            if pos == count:
                ans.append("".join(string))
                return

            string[positions[pos]] = string[positions[pos]].lower()
            recursion(string, pos+1)
            string[positions[pos]] = string[positions[pos]].upper()
            recursion(string, pos+1)

        recursion(s, 0)
        return ans

            