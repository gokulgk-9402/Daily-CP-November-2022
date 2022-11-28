class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        loss = defaultdict(int)
        players = set()

        for w,l in matches:
            loss[l] += 1
            players.add(w)
            players.add(l)

        for player in players:
            if loss[player] == 0:
                ans[0].append(player)
            elif loss[player] == 1:
                ans[1].append(player)

        ans[0].sort()
        ans[1].sort()

        return ans