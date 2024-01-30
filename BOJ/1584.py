import sys
from heapq import heappop, heappush
input = sys.stdin.readline


graph = [[0] * 501 for _ in range(501)]

# 위험한 구역
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    r1, r2 = min(x1, x2), max(x1, x2)
    c1, c2 = min(y1, y2), max(y1, y2)

    for i in range(c1, c2+1):
        for j in range(r1, r2+1):
            graph[i][j] = 1

# 죽음의 구역
m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    r1, r2 = min(x1, x2), max(x1, x2)
    c1, c2 = min(y1, y2), max(y1, y2)

    for i in range(c1, c2+1):
        for j in range(r1, r2+1):

            graph[i][j] = 2

q = []
visited = [[False]* 501 for _ in range(501)]
heappush(q, (0, 0, 0))

while q:

    cnt, x, y = heappop(q)

    if x == 500 and y == 500:
        print(cnt)
        exit(0)

    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy

        if 0 <= nx <= 500 and 0 <= ny <= 500 and graph[ny][nx] != 2 and not visited[ny][nx]:
            heappush(q, (cnt+graph[ny][nx], nx, ny))
            visited[ny][nx] = True

print(-1)