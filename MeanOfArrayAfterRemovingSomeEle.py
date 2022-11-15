class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        to_rmv = (5*n)//100

        print(to_rmv)

        s = sum(arr[to_rmv:-to_rmv])
        s = s/(n-2*to_rmv)

        return s