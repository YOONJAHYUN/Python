import sys

sys.stdin = open('input.txt')

def killing_flies():
    result = 0
    for i in range(N):
        for j in range(N):
            ans1 = 0
            ans1 += data[i][j]
            for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):   # 상 하 좌 우

                for mul in range(1, M):
                    ni, nj = i + di*mul, j + dj*mul

                    if 0 <= ni < N and 0 <= nj < N:
                        ans1 += data[ni][nj]

            ans2 = 0
            ans2 += data[i][j]
            for di, dj in ((1, 1), (-1, -1), (1, -1), (-1, 1)):  # 상 하 좌 우

                for mul in range(1, M):
                    ni, nj = i + di * mul, j + dj * mul

                    if 0 <= ni < N and 0 <= nj < N:
                        ans2 += data[ni][nj]
            result = max(result, ans1, ans2)

    return result


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', killing_flies())
