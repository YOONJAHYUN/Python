import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, -1, 1, 0, -1, 1]

    result = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                if 0 <= i+dy[k] < N and 0 <= j+dx[k] < M:
                    if data[i+dy[k]][j+dx[k]] < data[i][j]:
                        cnt += 1
            if cnt >= 4:
                result += 1
    print(f'#{tc}', result)
