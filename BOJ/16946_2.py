import sys
from collections import deque
input = sys.stdin.readline

def BFS(y, x):

    count = 1
    my_visited = []

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == '0' and visited[ny][nx] not in my_visited:
                count += dict[visited[ny][nx]]
                my_visited.append(visited[ny][nx])

    return str(count % 10)


n, m = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]
my_idx = 1
dict = dict()
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0' and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = my_idx
            cnt = 0

            while q:
                y, x = q.popleft()
                cnt += 1

                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < m:
                        if not visited[ny][nx] and arr[ny][nx] == '0':
                            visited[ny][nx] = my_idx
                            q.append((ny, nx))
            dict[my_idx] = cnt
            my_idx += 1

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
