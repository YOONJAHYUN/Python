import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
    q = []

    heappush(q, start)

    while q:
        distance, now = heappop(q)

        if visited[now] < distance:
            continue

        for i in graph[now]:
            res = distance + i[0]

            if res < visited[i[1]]:
                visited[i[1]] = res
                heappush(q, (res, i[1]))


# n 도시의 개수, m 도로의 개수, k 거리 정보, x 도시의 정보
# 단방향임
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [int(1e9)] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1,b))
visited[x] = 0
dijkstra((0,x))
if k not in visited:
    print(-1)
else:
    for i in range(1, n+1):
        if visited[i] == k:
            print(i)
