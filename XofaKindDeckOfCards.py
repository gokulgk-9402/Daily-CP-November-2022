class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        mem = Counter(deck)
        lst = list(mem.values())
        minimum = min(lst)

        for i in range(2, minimum+1):
            flag = True
            for ele in lst:
                if ele%i:
                    flag = False
                    break

            if flag:
                return True

        return False