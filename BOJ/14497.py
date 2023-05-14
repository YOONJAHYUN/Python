import sys
from collections import deque
input = sys.stdin.readline

def BFS(y, x):

    q = deque()
    q.append((0, y, x))


    while q:

        cnt, sy, sx = q.popleft()

        if visited[sy][sx] < cnt:
            continue

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = sy+dy, sx+dx

            if 0 <= ny < n and 0 <= nx < m:
                if data[ny][nx] == '1':
                    if visited[ny][nx] > cnt +1:
                        visited[ny][nx] = cnt + 1
                        q.append((cnt+1, ny, nx))
                else:
                    if visited[ny][nx] > cnt:
                        visited[ny][nx] = cnt
                        q.appendleft((cnt, ny, nx))



n, m = map(int, input().split())

x1, y1, x2, y2 = map(int, input().split())

data = [list(input().rstrip()) for _ in range(n)]

INF = int(1e9)

visited = [[INF]*m for _ in range(n)]

BFS(x1-1, y1-1)

print(visited[x2-1][y2-1]+1)