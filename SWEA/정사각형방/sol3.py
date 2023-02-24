import sys

sys.stdin = open('input.txt')

def room_route(i, j):
    q = []
    alst = []

    q.append((i, j))# [1] 초기데이터 삽입
    visited[i][j] = 1
    alst.append(rooms[i][j])

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci+di, cj+dj

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and abs(rooms[ci][cj]-rooms[ni][nj]) == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                alst.append(rooms[ni][nj])

    return min(alst), len(alst)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    ans, cnt = N*N, 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                t, tcnt = room_route(i, j)

                if cnt < tcnt or (cnt == tcnt and ans > t):
                    ans, cnt = t, tcnt

    print(f'#{tc}', ans, cnt)