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

    result = 1
    while result:
        if not stack:
            if 0 <= dot[0] + dy[k] < N and 0 <= dot[1] + dx[k] < N:
                if mat[dot[0] + dy[k]][dot[1] + dx[k]] == 3:
                    print(f'#{tc}', 1)
                    break
                else:
                    print(f'#{tc}', 0)
                    break
        dot = stack.pop()

        for k in range(4):

            if 0 <= dot[0] + dy[k] < N and 0 <= dot[1] + dx[k] < N:

                if mat[dot[0] + dy[k]][dot[1] + dx[k]] == 0:

                    stack.append([dot[0] + dy[k], dot[1] + dx[k]])
                    mat[dot[0] + dy[k]][dot[1] + dx[k]] = 1

                if mat[dot[0] + dy[k]][dot[1] + dx[k]] == 3:
                    print(f'#{tc}', 1)
                    result = 0











