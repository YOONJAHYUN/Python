import sys
sys.setrecursionlimit(10**6)
for test_case in range(int(input())):
    M, N, E = map(int, input().split())
    node = [[0]*M for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0
    for _ in range(E):
        x, y = map(int, input().split())
        node[y][x] = 1

    def dfs(y, x):
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if N > ny >= 0 and M > nx >= 0:
                if node[ny][nx] == 1:
                    node[ny][nx] = 0
                    dfs(ny, nx)

    for y in range(N):
        for x in range(M):
            if node[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)