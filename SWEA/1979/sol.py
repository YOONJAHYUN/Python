import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    # 행렬 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행렬 90도 회전 만들기
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][N-1-j] = arr[j][i]

    # print(new_arr)

    # 행렬에서 가로로 1이 연속인 것 찾기
    result1 = 0

    for i in range(N):
        count1 = 0
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1] == 1:
                count1 += 1
            else:
                if i == N-1:
                    result1 += 1
                else:
                    count1 = 0
            if j == N-1:
                if count1 == K-1:
                    result1 += 1

    # 90도 회전 행렬에서 가로로 1이 연속인 것 찾기
    result2 = 0
    for i in range(N):
        count2 = 0
        for j in range(1, N):
            if new_arr[i][j] == new_arr[i][j-1] == 1:
                count2 += 1
            else:
                if count2 == N-1:
                    result2 += 1
                else:
                    count2 = 0
            if j == N - 1:
                if count2 == K-1:
                    result2 += 1


    print(result1 + result2)
