import sys
from collections import deque
input = sys.stdin.readline

'''
벽을 최소로 부숴야하기때문에 그냥 갈 수 있으면 가고, 아니라면 벽을 부수는 형태로..
힙을 활용해서 0으로 지정된걸 먼저 뺌..
'''


# 가로 M 세로 N
m, n = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

INF = int(1e9)
# 시작점
q = deque([[0, 0, 0]])
d = [[INF] * m for _ in range(n)]
d[0][0] = 0

while q:
    cnt, y, x = q.popleft()

    if d[y][x] < cnt:
        continue

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y+dy, x+dx

        if 0 <= ny < n and 0 <= nx < m:
            if maze[ny][nx] == 1:
                if d[ny][nx] > cnt + 1:
                    d[ny][nx] = cnt + 1
                    # 부순거는 맨뒤
                    q.append([cnt+1, ny, nx])
            else:
                if d[ny][nx] > cnt:
                    d[ny][nx] = cnt
                    # 안부쉈으니 맨 앞
                    q.appendleft([cnt, ny, nx])
print(d[-1][-1])