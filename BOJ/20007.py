import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

n, m, x, y = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [INF] * n
visited[y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def dijkstra(start):

    q = []
    heappush(q, start)

    while q:

        distance, now = heappop(q)

        if visited[now] < distance:
            continue

        for next_dis, next_home in graph[now]:
            total_dis = distance + next_dis
            if total_dis < visited[next_home]:
                visited[next_home] = total_dis
                heappush(q, (total_dis, next_home))

dijkstra((0, y))

visited.sort()

answer = 0

if visited[-1] * 2 > x:
    print(-1)
else:
    temp = 0
    for i in range(n):
        home = visited[i]

        if temp + home * 2 > x:
            temp = home * 2
            answer += 1
        else:
            temp += home * 2

    if temp:
        answer += 1
    print(answer)
