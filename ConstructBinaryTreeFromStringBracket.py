from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def treeFromString(self, s : str) -> Optional['Node']:
        # code here
        
        def get_index(string, start, end):
            if start > end:
                return -1
            t = []
            for i in range(start, end + 1):
                # print(t)
                if string[i] == "(":
                    t.append("(")
                elif string[i] == ")":
                    if t:
                        t.pop()
                        if not t:
                            return i
            
            return -1
        
        def helper(string, start, end):
            if start > end:
                return None
            val = ""
            while start < len(string) and ord("0")<=ord(string[start])<=ord("9"):
                val += string[start]
                start += 1
            # print(val)
            node = Node(int(val))
            index = -1
            if start <= end and string[start] == "(":
                # print(string, start, end)
                index = get_index(string, start, end)
            if index != -1:
                node.left = helper(string, start+1, index-1)
                node.right = helper(string, index+2, end-1)
            return node
            
        return helper(s, 0, len(s)-1)