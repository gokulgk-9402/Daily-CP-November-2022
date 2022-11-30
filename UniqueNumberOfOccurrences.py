class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctr = Counter(arr)
        ctr2 = Counter(ctr.values())

        for key in ctr2:
            if ctr2[key] != 1:
                return False

        return True