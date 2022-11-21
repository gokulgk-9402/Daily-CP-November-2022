class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        graph = defaultdict(int)
        mem2 = defaultdict(int)

        for u,v in edges:
            graph[u] += 1
            graph[v] += 1
            if v < u:
                u,v = v,u
            mem2[(u,v)] += 1

        lst = sorted(graph.values())
        lst = [0]*(n-len(lst)) + lst

        ans = []
        for query in queries:
            t = sum(n-bisect.bisect(lst, query-lst[i]) for i in range(n))
            t -= n - bisect.bisect(lst, query//2)
            t = t // 2

            for x,y in mem2:
                t += (graph[x] + graph[y] - mem2[(x,y)]) > query
                t -= (graph[x] + graph[y]) > query

            ans.append(t)

        return ans