import sys
from collections import deque
input = sys.stdin.readline

def tomato_box():
    day = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] > day:
                    day = tomatos[i][j][k]

                if tomatos[i][j][k] == 0:
                    print(-1)
                    return
    print(day-1)
    return

# M 상자 가로길이, N 상자 세로길이, H 상자의 수(높이)
M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dir = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, -1], [0, -1, 0], [-1, 0, 0]]
q = deque()
cnt1 = 0
cnt2 = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 1:
                q.append([i, j, k])
                cnt1 += 1
            if tomatos[i][j][k] == -1:
                cnt2 += 1

if cnt1 + cnt2 == M*N*H:
    print(0)
else:

    while q:
        ni, nj, nk = q.popleft()

        for di, dj, dk in dir:

            si, sj, sk = ni + di, nj + dj, nk + dk

            if 0<= si < H and 0 <= sj < N and 0 <= sk < M and tomatos[si][sj][sk] == 0:
                tomatos[si][sj][sk] = tomatos[ni][nj][nk] + 1
                q.append([si, sj, sk])


    tomato_box()

