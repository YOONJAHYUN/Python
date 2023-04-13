import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 1e9
def dijkstra(start):
    visited[start[1]] = 0

    heap = []

    heappush(heap, start)

    while heap:

        distance, now = heappop(heap)

        if distance > visited[now]:
            continue

        for new_distance, next in graph[now]:
            res = new_distance + distance
            if res < visited[next]:
                visited[next] = res
                heappush(heap, (res, next))

    return


# V 정점의 개수, E 간선의 개수
V, E = map(int, input().split())

# K 시작 정점의 번호
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

visited = [INF] * (V+1)
dijkstra((0, K))
# print(visited)
for i in range(1, V+1):
    if visited[i] == INF:
        print('INF')
    else:
        print(visited[i])

