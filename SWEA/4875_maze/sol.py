import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 0 통로 1 벽 2출발 3도착
    N = int(input())
    mat = [list(map(int, input().rstrip())) for _ in range(N)]
    # print(mat)
    x = 0
    y = 0
    # 출발지를 먼저 찾아.
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                x = j # 출발지 x좌표
                y = i # 출발지 y좌표

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    stack = [[y, x]]
    while True: # 탈출구를 찾을때까지 while문을 순회한다.

        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
                if mat[stack[0] + dy[i]][stack[1] + dx[i]] == 0:
                    mat[y][x] = 1
                    x = x + dx[i]
                    y = y + dy[i]
                elif mat[y + dy[i]][x + dx[i]] == 3:
                    result = 1
                    break
        # else:
        #     result = 0
        #     break


    print(f'#{tc}', result)
