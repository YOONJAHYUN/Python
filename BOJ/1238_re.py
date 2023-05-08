import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start):
    v = [int(1e9)] * (n + 1)
    v[start[1]] = 0
    q = []
    heappush(q, start)

    while q:

        time, now = heappop(q)

        if v[now] < time:
            continue

        for now_time, next in graph[now]:
            # print(now_time, next)
            total = now_time + time

            if total < v[next]:
                v[next] = total

                heappush(q, (total, next))

    if start[1] == x:
        return v
    else:
        return v[x]

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

back = dijkstra((0, x))

ans = 0
for i in range(1, n+1):
    if i != x:
        ans = max((dijkstra((0, i))+back[i]), ans)
print(ans)