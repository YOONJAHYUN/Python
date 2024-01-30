import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

arr = []
# visited = [[False] * m for _ in range(n)]
q = deque()

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 1:
            q.append((i, j, 0))
            # visited[i][j] = True
    arr.append(lst)

ans = -1

while q:

    y, x, cnt = q.popleft()

    for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ny, nx = dy + y, dx + x
        if 0 <= ny < n and 0 <= nx < m and not arr[ny][nx]:
            # visited[ny][nx] = True
            arr[ny][nx] = 1
            q.append((ny, nx, cnt+1))
            ans = cnt

for i in range(n):
    if 0 in arr[i]:
        print(-1)
        exit(0)

print(cnt)


