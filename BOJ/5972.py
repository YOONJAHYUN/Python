import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(cost, start):

    q = []
    heappush(q, (cost, start))

    while q:
        c, now = heappop(q)

        if v[now] < cost:
            continue
        for i in graph[now]:
            res = c + i[0]

            if res < v[i[1]]:
                v[i[1]] = res
                heappush(q, (res, i[1]))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

v = [int(1e9)] * (n+1)
for _ in range(m):
    # a , b 헛간 c 소
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dijkstra(0, 1)
print(v[n])


