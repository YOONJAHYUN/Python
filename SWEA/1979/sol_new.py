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
        count = 0
        # count_save = 0
        for j in range(1, N):
            # 연속된 숫자가 1로 같으면 count를 up 해준다.
            if arr[i][j] == arr[i][j-1] == 1:
                count += 1
                # 마지막꺼에서 count가 K-1이라면, result up
                if (j == (N-1)) and (count == (K-1)):
                    result1 += 1
            # 연속된 숫자가 다르면, count에 있는 숫자가 K-1과 같은지 먼저 확인한다.
            else:
                # K-1과 같다면, result1를 up 해주고 count를 초기화 해준다.
                if count == K-1:
                    result1 += 1
                    count = 0
                # 같지않다면, count를 초기화 해준다.
                else:
                    count = 0


    # 회전한 행렬에서 가로로 1이 연속인 것 찾기
    result2 = 0
    for i in range(N):
        count = 0
        # count_save = 0
        for j in range(1, N):
            # 연속된 숫자가 1로 같으면 count를 up 해준다.
            if new_arr[i][j] == new_arr[i][j - 1] == 1:
                count += 1
                if (j == (N-1)) and (count == (K-1)):
                    result2 += 1
            # 연속된 숫자가 다르면, count에 있는 숫자가 K-1과 같은지 먼저 확인한다.
            else:
                # K-1과 같다면, result2를 up 해주고 count를 초기화 해준다.
                if count == K - 1:
                    result2 += 1
                    count = 0
                # 같지않다면, count를 초기화 해준다.
                else:
                    count = 0


    print(f'#{tc+1}', result1+result2)