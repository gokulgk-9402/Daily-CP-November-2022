from collections import defaultdict
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        comp = defaultdict(int)
        cols = defaultdict(list)
        s = defaultdict(int)

        for y,x in stones:
            comp[y] = y
            cols[x].append(y)

        def parent(i):
            if comp[i] == i:
                return i

            comp[i] = parent(comp[i])
            return comp[i]

        for x in cols:
            ch = min(cols[x])
            if ch in comp:
                ch = parent(ch)

            for y in cols[x]:
                if y not in comp:
                    comp[y] = ch
                else:
                    comp[parent(y)] = ch
        
        for y,x in stones:
            s[parent(y)] += 1

        ans = sum([s[x]-1 for x in s])

        return ans