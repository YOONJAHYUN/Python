import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    my_max1 = 0
    for i in range(N):
        cnt = 0
        for j in range(M-1):
            if mat[i][j] == mat[i][j+1] == 1:
                cnt += 1
        my_max1 = max(my_max1, cnt+1)

    my_max2 = 0
    for j in range(M):
        cnt = 0
        for i in range(N - 1):
            if mat[i][j] == mat[i+1][j] == 1:
                cnt += 1
        my_max2 = max(my_max2, cnt + 1)

    print(f'#{tc}', max(my_max1, my_max2))