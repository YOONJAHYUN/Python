import sys

sys.stdin = open('input.txt')

# 가능한 모든 경로에 대한 합 계산

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    # arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]+ [[0]*(N+2)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for i in arr:
    #     print(i)
    # print()
    # print(arr)
    data = [[0] * N for _ in range(N)]
    # 마지막까지 도착 할 수 있는 루트는 총 2개.
    # 최대한 적게 더하면서 가야됨

    for i in range(N):
        for j in range(N):
            if 0 <= i-1 < N:
                num1 = data[i-1][j]
            else:
                num1 = 0

            if 0 <= j-1 < N:
                num2 = data[i][j-1]
            else:
                num2 = 0
            if num1 > 0 and num2 > 0:
                data[i][j] = arr[i][j] + min(num1, num2)
            else:
                data[i][j] = arr[i][j] + max(num1, num2)


    print(f'#{tc}', data[N-1][N-1])