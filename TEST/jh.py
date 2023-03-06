import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, p = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):

        for j in range(n):
            cnt = 0
            cnt += data[i][j]
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                for mul in range(1, p+1):
                    nx, ny = j + dx*mul, i + dy*mul

                    if 0 <= nx < n and 0 <= ny < n:
                        cnt += data[ny][nx]

            total = max(cnt, total)


    print(f'#{tc}', total)