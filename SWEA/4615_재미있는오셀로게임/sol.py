import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 처음엔 가운데에 배치

    # 1은 흑돌
    # 2는 백돌
    arr = [[0]*N for _ in range(N)]
    lo = int(N / 2)
    # 초기값 설정
    arr[lo][lo], arr[lo-1][lo-1], arr[lo-1][lo], arr[lo][lo-1] = 2, 2, 1, 1

    print(arr)

    # 상하좌우 대각선까지 모두 8방향 확인해야함
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, -1, 1]

    for n in range(M):


        X, Y, color = map(int, input().split())
        x = X - 1
        y = Y - 1

        arr[y][x] = color

        if

