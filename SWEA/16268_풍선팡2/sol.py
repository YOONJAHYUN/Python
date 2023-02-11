import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]

    result = 0
    for i in range(N):
        for j in range(M):
            my_sum = 0
            for k in range(5):
                if 0 <= i+dy[k] < N and 0 <= j+dx[k] < M:
                    my_sum += arr[i+dy[k]][j+dx[k]]
            # result 갱신
            result = max(result, my_sum)

    print(f'#{tc}', result)

