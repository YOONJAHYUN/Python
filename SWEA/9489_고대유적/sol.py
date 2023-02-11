import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N개의 줄
    # M개의 데이터
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        count = 0
        for j in range(M-1):
            if arr[i][j] == arr[i][j+1] == 1:
                count += 1
                if j == M-2:
                    result.append(count + 1)

            else:
                if arr[i][j-1] == 1:
                    result.append(count + 1)
                count = 0

    for j in range(M):
        count = 0
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j] == 1:
                count += 1
                if i == N-2:
                    result.append(count + 1)

            else:
                if arr[i-1][j] == 1:
                    result.append(count + 1)
                count = 0



    print(f'#{tc}', max(result))