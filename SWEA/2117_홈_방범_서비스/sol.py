import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    # 운영 비용 = K*K + (K-1) * (K-1)
    cost = M*M -
    n = 2*M-1
    service = [[0]*n for _ in range(n)]
    idx = 0

    # 서비스영역 면적
    for i in range(n):
        for j in range(-idx, idx+1):

            service[i][M-1+j] = 1

        if i <= M-2:
            idx += 1

        else:
            idx -= 1

    result = []
    for i in range(0, N-n+1):
        for j in range(0, N-n+1):
            cnt = 0
            for k in range(n):
                for l in range(n):
                   if data[i+k][j+l] + service[k][l] == 2:
                       cnt += 1

            result.append(cnt)
    if result:
        print(f'#{tc}', max(result))


