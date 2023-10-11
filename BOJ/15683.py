import sys
from copy import deepcopy
input = sys.stdin.readline

def check(d, data):
    global answer

    if d == len(cctvs):
        ans = 0
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    ans += 1
        answer = min(ans, answer)
        return

    t, y, x = cctvs[d]
    for lst in cctv_moving[t]:
        data1 = deepcopy(data)
        for dx, dy in lst:
            mul = 1

            while True:
                ny, nx = y+dy*mul, x+dx*mul

                if 0 > ny or ny >= n or 0 > nx or nx >= m:
                    break

                if data1[ny][nx] == 6:
                    break
                elif data1[ny][nx] == 0:
                    data1[ny][nx] = -1

                mul += 1

        check(d+1, data1)


# 세로 가로
n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

# x좌표 y좌표
cctv_moving = {
    1 : [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]],
    2 : [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    3 : [[(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]],
    4 : [[(1, 0), (0, -1), (-1, 0)], [(1, 0), (-1, 0), (0, 1)], [(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)]],
    5 : [[(1, 0), (-1, 0), (0, 1), (0, -1)]]
}

cctvs = []
answer = int(1e9)
for i in range(n):
    for j in range(m):
        if data[i][j] not in [0, 6]:
            cctvs.append((data[i][j],i,j))



check(0, deepcopy(data))


print(answer)