import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):

    q = deque()
    q.append((i, j, 0))
    if arr[i][j]:
        return [i, j, arr[i][j], 0]

    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True

    flag = -1
    temp = []
    while q:
        y, x, cnt = q.popleft()

        if len(temp) == 0 and arr[y][x] > 1:
            flag = cnt
            temp.append([y, x, arr[y][x], cnt])
        elif arr[y][x] > 1 and flag == cnt:
            temp.append([y, x, arr[y][x], cnt])
        elif len(temp) > 0 and cnt > flag:
            break

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cnt+1))

    if temp:
        temp.sort()
        return temp[0]
    else:
        return False


n, m, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

Y, X = map(int, input().split())
Y -= 1
X -= 1
data = []

selected = [False] * m

for i in range(2, m+2):
    a, b, c, d = map(int, input().split())
    data.append((a-1, b-1, c-1, d-1))
    arr[a-1][b-1] = i

while True:
    res = BFS(Y, X)

    if not res:
        if False in selected:
            print(-1)
            break
        print(fuel)
        break

    py, px, idx, cnt = res

    fuel -= cnt
    if fuel < 0:
        print(-1)
        break

    dir_y, dir_x = data[idx-2][2], data[idx-2][3]
    q = deque()
    q.append((py, px, 0))
    visited = [[False] * n for _ in range(n)]
    visited[py][px] = True

    ans = 0
    while q:
        sy, sx, count = q.popleft()

        if sy == dir_y and sx == dir_x:
            fuel -= count
            ans = count
            break

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = sy+dy, sx+dx
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, count+1))
    else:
        print(-1)
        break
    if fuel < 0:
        print(-1)
        break
    fuel += ans * 2
    Y, X = dir_y, dir_x
    selected[idx-2] = True
    arr[py][px] = 0






