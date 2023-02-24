import sys

sys.stidn = open('input.txt')

# 터널

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    tunnel = [[],
              [(0, 1), (0, -1), (1, 0), (-1, 0)],   # 1
              [(1, 0), (-1, 0)],                    # 2
              [(0, 1), (0, -1)],                    # 3
              [(-1, 0), (0, 1)],                    # 4
              [(0, 1), (1, 0)],                     # 5
              [(0, -1), (1, 0)],                    # 6
              [(-1, 0), (0, -1)]]                   # 7
    q = []
    q.append((y, x))
    visited = []
    visited.append((y, x))
    hole = (R, C)
    data[R][C]

    def gogo(y, x):
        y, x = q.pop(0)

        if data[y][x] == 1:
            for i in tunnel[1]:
                ny, nx = i[0], i[1]
                if ny == visited[-1][0] and nx == visited[-1][1]:
                    q.append((y + ny, x + nx))
                    visited.append((y, x))

        elif data[y][x] == 2:

        elif data[y][x] == 3:
            for i in tunnel[3]:
                ny, nx = i[0], i[1]
                q.append((y+ ny, x + nx))
                visited.append((y, x))
        elif data[y][x] == 4:

        elif data[y][x] == 5:

        elif data[y][x] == 6:

        elif data[y][x] == 7: