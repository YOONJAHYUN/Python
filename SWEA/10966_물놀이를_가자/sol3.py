import sys

sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    data = []
    q = deque()

    for _ in range(N):
        data.append(list(input().rstrip()))

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    result = 0

    for i in range(N):
        for j in range(M):
            if data[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    while q:
        si, sj = q.popleft()

        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[si][sj] + 1
                result += visited[ni][nj]
            for i in visited:
                print(i)
            print()
    print(f'#{tc}',result)