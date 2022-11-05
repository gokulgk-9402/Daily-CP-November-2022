class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        heights = []

        maximum = 0

        for i in range(len(positions)):
            left, side = positions[i]
            base = 0
            for j in range(i):
                prev_l, prev_s = positions[j]
                if left+side <= prev_l or left>=prev_l+prev_s:
                    continue
                base = max(base, heights[j])

            heights.append(base + side)
            maximum = max(maximum, heights[-1])
            ans.append(maximum)

        return ans