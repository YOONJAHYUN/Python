import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(start, end):

    q = deque()
    q.append(start)

    while q:
        now_node = q.popleft()

        for next_cost, next_node in graph[now_node]:
            if visited[next_node] < next_cost + visited[now_node]:
                continue
            visited[next_node] = next_cost + visited[now_node]
            q.append(next_node)

    print(visited[end])

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = 1e9
visited = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s, t = map(int, input().split())

visited[s] = 0
dijkstra(s, t)