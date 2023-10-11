import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstarta(start):
    q = []
    heappush(q, start)

    while q:

        time, now = heappop(q)

        if visited[now] < time or data[now]:
            continue

        for next_time, next in graph[now]:

            total = next_time + time

            if total < visited[next] and (not data[next] or next == n - 1):
                visited[next] = total
                heappush(q, (total, next))


n, m = map(int, input().split())

data = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
visited = [int(1e11) for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

dijkstarta((0, 0))
if visited[n - 1] == int(1e11):
    print(-1)
else:
    print(visited[n - 1])
