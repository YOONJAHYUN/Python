import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = int(1e9)
# 좌, 상, 하, 우
DIR = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def dijkstra(y, x):

    q = []
    visited = [[INF] * w for _ in range(h)]
    check = [[[False]*4 for _ in range(w)] for _ in range(h)]
    # 초기값 넣어주기
    for k in range(4):
        sy, sx = y + DIR[k][0], x + DIR[k][1]

        if sy >= h or sy < 0 or sx >= w or sx < 0 or arr[sy][sx] == "*":
            continue
        visited[sy][sx] = 0
        check[sy][sx] = [True] * 4
        heappush(q, (0, sy, sx, k))

    visited[y][x] = 0

    while q:

        cnt, ny, nx, dir = heappop(q)

        if arr[ny][nx] == "C":
            print(cnt)
            # for i in visited:
            #     print(i)
            return

        for k in range(4):
            sy, sx = ny+DIR[k][0], nx+DIR[k][1]

            if sy >= h or sy < 0 or sx >= w or sx < 0 or k+dir == 3:
                continue

            now = 0 if k == dir else 1

            if arr[sy][sx] != "*" and visited[sy][sx] >= cnt + now and not check[sy][sx][k]:
                visited[sy][sx] = cnt+now
                check[sy][sx][k] = True
                heappush(q, (cnt+now, sy, sx, k))


w, h = map(int, input().split())

arr = [input().rstrip() for _ in range(h)]

# 100 * 100 = 10000
for i in range(h):
    for j in range(w):
        if arr[i][j] == "C":
            dijkstra(i, j)
            exit(0)



