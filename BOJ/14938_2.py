import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):
    visited = [1e9]*(n+1)
    visited[start[1]] = 0
    heap = []

    heappush(heap, start)

    while heap:
        distance, now = heappop(heap)

        if visited[now] < distance:
            continue

        for new_distance, next in graph[now]:
            res = new_distance + distance
            if visited[next] > res:
                visited[next] = res

                heappush(heap, (res, next))
    return visited


n, m, r = map(int, input().split())

t = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())

    graph[a].append((l, b))
    graph[b].append((l, a))

result = 0
for num in range(1, n+1):
    ans = 0
    v = dijkstra((0, num))

    for i in range(1, n+1):
        if v[i] <= m:
            ans += t[i-1]
    result = max(ans, result)
print(result)
