from typing import List

class Solution:
    def largestArea(self,n:int,m:int,k:int, enemy : List[List[int]]) -> int:
        # code here
        x=[ene[0] for ene in enemy]
        y=[ene[1] for ene in enemy]
        x.append(0)
        x.append(n+1)
        y.append(0)
        y.append(m+1)
        x.sort()
        y.sort()
        maxx=0
        maxy=0
        for i in range(1,len(x)):
            maxx=max(maxx,x[i]-x[i-1]-1)
        for i in range(1,len(y)):
            maxy=max(maxy,y[i]-y[i-1]-1)
        return maxx*maxy