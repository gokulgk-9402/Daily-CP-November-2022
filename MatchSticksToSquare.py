class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        number = len(matchsticks)
        if number == 0:
            return False
        if perimeter%4:
            return False

        side = perimeter//4

        matchsticks.sort(reverse=True)
        side_lens = [0]*4

        def dfs(index):
            if index == number:
                return side_lens[0] == side_lens[1] == side_lens[2] == side

            for i in range(4):
                if side_lens[i] + matchsticks[index] <= side:
                    side_lens[i] += matchsticks[index]

                    if dfs(index+1):
                        return True

                    side_lens[i] -= matchsticks[index]
                
            return False

        return dfs(0)