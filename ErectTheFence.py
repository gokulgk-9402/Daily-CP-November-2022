from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p1, p2, p3):
            return (p3[1] - p2[1]) * (p2[0] - p1[0]) - (p3[0] - p2[0]) * (p2[1] - p1[1])
        
        length = len(trees)

        if length == 1:
            return trees

        trees = [tuple(x) for x in trees]
        trees.sort()
                
        lower = []
        curr = 0
        for tree in trees:
            while curr >= 2 and orientation(lower[-2], lower[-1], tree) < 0:
                lower.pop()
                curr -= 1
            lower.append(tree)
            curr += 1
            
        upper = []
        curr = 0
        for tree in trees:
            while curr >= 2 and orientation(upper[-2], upper[-1], tree) > 0:
                upper.pop()
                curr -= 1
            upper.append(tree)
            curr += 1
            
        return list(set(lower + upper))