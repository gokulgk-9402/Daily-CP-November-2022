# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        
        while low <= high:
            num = (low+high)//2
            r = guess(num)
            if r == 0:
                return num
            if r == -1:
                high = num - 1
            else:
                low = num + 1
            
            num = random.randrange(low, high+1)
            r = guess(num)

        return num