import sys
from collections import deque
input = sys.stdin.readline

def BFS(y, x):

    q = deque()
    # 현재위치 y, x, 전체능력, 말능력
    q.append((y, x, 0, 0))
    v1[y][x] = True
    v2[y][x] = True
    while q:

        ny, nx, cnt, horse = q.popleft()
        # print(ny, nx, cnt, horse)

        # 종료조건
        if ny == h-1 and nx == w-1:
            print(cnt)
            return

        # 말 능력이 남았을 때
        if horse < k:

            for dy, dx in ((2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (2, -1), (1, -2)):
                sy = ny + dy
                sx = nx + dx

                if 0 <= sy < h and 0 <= sx < w and not data[sy][sx] and v1[sy][sx] > horse+1:
                    q.append((sy, sx, cnt+1, horse+1))
                    v1[sy][sx] = horse+1

        # 그냥 인접
        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            sy = ny + dy
            sx = nx + dx

            if 0 <= sy < h and 0 <= sx < w and not data[sy][sx] and v2[sy][sx] > horse:
                q.append((sy, sx, cnt + 1, horse))
                v2[sy][sx] = horse

    print(-1)


k = int(input())
w, h = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(h)]
v1 = [[int(1e9)]*w for _ in range(h)]
v2 = [[int(1e9)]*w for _ in range(h)]

'''
y, x
(2, 1), (1, 2), (-1, 2), (-2, 1), ... 로 가는건 k번

(1, 0), ... 으로 가는 건 상관 없음

최소한으로 가야됨

1
3 4
0 0 0
1 1 0
1 1 1
1 0 0

'''

BFS(0, 0)