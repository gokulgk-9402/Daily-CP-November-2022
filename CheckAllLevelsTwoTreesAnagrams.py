from typing import Optional
from collections import deque, defaultdict
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        # code here
        mem1 = defaultdict(list)
        mem2 = defaultdict(list)
        
        q1 = deque([(node1, 1)])
        q2 = deque([(node2, 1)])
        
        while q1:
            n,d = q1.popleft()
            if not n:
                continue
            mem1[d].append(n.data)
            q1.append((n.left, d+1))
            q1.append((n.right, d+1))
            
        while q2:
            n,d = q2.popleft()
            if not n:
                continue
            mem2[d].append(n.data)
            q2.append((n.left, d+1))
            q2.append((n.right, d+1))
            
        for key in mem1:
            mem1[key].sort()
        for key in mem2:
            mem2[key].sort()
            
        if list(mem1.keys()) != list(mem2.keys()):
            return False
            
        for key in mem1:
            if mem1[key] != mem2[key]:
                return False
                
        return True