import sys
from collections import deque
input = sys.stdin.readline


def BFS(i, j):
    global answer

    visited = [[False] * m for _ in range(n)]
    q = deque()
    visited[i][j] = 1
    q.append((i, j, 1))

    while q:
        y, x, cnt = q. popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == "L" and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cnt+1))
                answer = max(answer, cnt)



n, m = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            BFS(i, j)


print(answer)


