class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):

            temp = nums[l[i]:r[i]+1]
            temp.sort()

            if len(temp) <= 2:
                ans.append(True)

            else:
                flag = True
                diff = temp[1] - temp[0]
                for i in range(2, len(temp)):
                    if temp[i] - temp[i-1] != diff and flag:
                        ans.append(False)
                        flag = False

                if flag:
                    ans.append(True)

        return ans