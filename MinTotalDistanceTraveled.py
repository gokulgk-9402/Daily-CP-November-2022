class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)

        mem = [float('inf')] * (n+1)
        mem[n] = 0
        robot.sort()
        factory.sort()

        for i in range(m-1, -1, -1):
            for j in range(n):
                curr = 0
                for k in range(1, min(factory[i][1], n-j) + 1):
                    curr += abs(robot[j+k-1] - factory[i][0])
                    mem[j] = min(mem[j], mem[j+k] + curr)

        return mem[0]