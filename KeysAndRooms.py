class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        q = deque([0])

        visited = [0 for _ in range(n)]

        while q:
            curr = q.popleft()

            if visited[curr]:
                continue
            visited[curr] = 1

            for key in rooms[curr]:
                q.append(key)

        if sum(visited) == n:
            return True

        return False
