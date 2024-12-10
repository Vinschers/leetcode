from collections import deque


class Solution:
    def bfs(self, adj, s):
        q = deque()
        visited = [False] * len(adj)
        dist = [0] * len(adj)

        visited[s] = True
        q.append(s)

        while q:
            u = q.popleft()

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    dist[v] = dist[u] + 1

        return dist

    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)

        answer = []

        for u, v in queries:
            adj[u].append(v)
            answer.append(self.bfs(adj, 0)[n - 1])

        return answer
