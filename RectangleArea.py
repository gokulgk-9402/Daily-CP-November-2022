class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        a1 = (ax2 - ax1) * (ay2 - ay1)
        a2 = (bx2 - bx1) * (by2 - by1)

        intersec_x = (min(by2, ay2) - max(ay1, by1)) 
        intersec_y = (min(bx2, ax2) - max(ax1, bx1))

        if intersec_x > 0 and intersec_y > 0:
            return a1 + a2 - (intersec_x*intersec_y)

        return a1 + a2