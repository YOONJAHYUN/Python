import sys
from collections import deque
sys.stdin = open('input.txt')
# BFS로 구현해야할 듯.

def finding_water(ii, jj):
    global water, data
    q = deque()
    q.append((ii, jj))
    visited = [[0] * M for _ in range(N)]

    while q:

        si, sj = q.popleft()

        for k in range(4):

            ni = si + di[k]
            nj = sj + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[si][sj] + 1

                if data[ni][nj] == 'W':
                    water += (visited[si][sj]+1)
                    return

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    data = []

    for _ in range(N):
        data.append(list(input().rstrip()))

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
    water = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'L':

                finding_water(i, j)

    print(f'#{tc}', water)
