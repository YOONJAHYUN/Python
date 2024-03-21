import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def BFS(lst):

    visited = [[False]*n for _ in range(n)]

    q = deque()

    count = 0
    my_wall = 0

    for i, j in lst:
        q.append((0, i, j))
        visited[i][j] = True

    while q:

        cnt, y, x = q.popleft()

        if arr[y][x] == 0:
            my_wall += 1
            count = max(cnt, count)

        if my_wall == wall:
            return count

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = y+dy, x+dx

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] != 1:
                visited[ny][nx] = True
                q.append((cnt+1, ny, nx))

    return n*n

n, m = map(int, input().split())
arr = []
virus = []
wall = 0
answer = n*n

for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(n):
        if lst[j] == 2:
            virus.append((i, j))
        elif lst[j] == 0:
            wall += 1

for combi in combinations(virus, m):
    # print(combi)
    answer = min(BFS(combi), answer)

if answer == n*n:
    print(-1)
else:
    print(answer)




