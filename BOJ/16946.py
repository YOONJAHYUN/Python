import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
    q = deque()
    q.append((i, j))
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    cnt = 0

    while q:
        y, x = q.popleft()
        cnt += 1

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and arr[ny][nx] == '0':
                    visited[ny][nx] = True
                    q.append((ny, nx))
    # print(cnt)
    return str(cnt)


n, m = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]
# print(arr)

result = []
for i in range(n):
    temp = ''
    for j in range(m):
        if arr[i][j] == '1':
            temp += BFS(i, j)
        else:
            temp += '0'
    result.append(temp)

for lst in result:
    print(lst)
