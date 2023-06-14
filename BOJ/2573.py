import sys
from collections import deque
input = sys.stdin.readline

'''
빙산이 처음으로 두덩어리로 되는 순간

상하좌우를 비교해서 0이라면 -1 한다. 근데 바로바로 하는게 아니라 보관했다가 한사이클이 끝나면 반환한다.
반환할때 bfs로 체크
'''


def BFS(y, x):
    visited = [[False]*m for _ in range(n)]

    my_cnt = 0
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        my_cnt += 1
        ny, nx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            sy = ny + dy
            sx = nx + dx
            if 0 <= sy < n and 0 <= sx < m and data[sy][sx] and not visited[sy][sx]:
                q.append((sy, sx))
                visited[sy][sx] = True

    # print(my_cnt, count)

    if my_cnt != count:
        print(ans)
        exit((0))




n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]


ans = 0
while True:
    result = [[0]*m for _ in range(n)]
    # 순회하면서 빙산에 녹을 양을 정한다.
    for i in range(n):
        for j in range(m):
            if data[i][j]:
                cnt = 0
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if not data[ni][nj]:
                            cnt += 1
                # 녹을 양을 표시함
                result[i][j] = cnt

    ny, nx = -1, -1
    count = 0
    # 녹은양 적용
    for i in range(n):
        for j in range(m):
            if data[i][j] - result[i][j] >= 0:
                data[i][j] -= result[i][j]
            else:
                data[i][j] = 0

            if data[i][j]:
                count += 1
                ny, nx = i, j
                # visited[i][j] = True
    # BFS돌리면서 빙하 연결이 되는지 확인
    if ny != -1 and nx != -1:
        ans += 1
        BFS(ny, nx)
    else:
        # 모두 녹을때까지 안나뉘어지면 0 출력
        print(0)
        exit(0)

