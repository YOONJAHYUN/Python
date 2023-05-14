import sys
from collections import deque
input = sys.stdin.readline

def BFS(y, x):
    q = deque()
    q.append((y, x, 0))

    while q:
        sy, sx, destroy = q.popleft()

        if sy == n-1 and sx == m-1:
            return visited[sy][sx][destroy]

        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ny, nx = sy + dy, sx + dx

            if 0 <= ny < n and 0 <= nx < m:
                # 벽 뚫기
                if data[ny][nx] and not destroy:
                    q.append((ny, nx, 1))
                    visited[ny][nx][1] = visited[sy][sx][0] + 1
                # 벽아닌경우
                elif not data[ny][nx] and not visited[ny][nx][destroy]:
                    q.append((ny, nx, destroy))
                    visited[ny][nx][destroy] = visited[sy][sx][destroy] + 1
    return -1


n, m = map(int, input().split())

data = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
print(BFS(0, 0))
