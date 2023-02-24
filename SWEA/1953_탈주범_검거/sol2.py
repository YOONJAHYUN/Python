import sys

sys.stdin = open('input.txt')

# 터널

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    maze = [[0]*2*M for _ in range(2*N)]
    # print(data)
    for i in range(N):
        for j in range(M):
            maze[2*i][2*j] = data[i][j]
    # 터널만들기
    for i in range(N):
        for j in range(M):
            if data[i][j] != 0:
                if data[i][j] == 1:
                    if 0 <= i + 1 < N and 0 <= j < M:
                        if data[i+1][j] == 1 or data[i+1][j] == 2 or data[i+1][j] == 4 or data[i+1][j] == 7:
                            maze[2*i+1][2*j] = 1
                    if 0 <= i < N and 0 <= j+1 < M:
                        if data[i][j+1] == 1 or data[i][j+1] == 3 or data[i][j+1] == 6 or data[i][j+1] == 7:
                            maze[2*i][2*j+1] = 1

                elif data[i][j] == 2:
                    if 0 <= i + 1 < N and 0 <= j < M:
                        if data[i+1][j] == 1 or data[i+1][j] == 2 or data[i+1][j] == 4 or data[i+1][j] == 7:
                            maze[2*i+1][2*j] = 1

                elif data[i][j] == 3:
                    if 0 <= i < N and 0 <= j + 1 < M:
                        if data[i][j+1] == 1 or data[i][j+1] == 3 or data[i][j+1] == 6 or data[i][j+1] == 7:
                            maze[2*i][2*j+1] = 1

                elif data[i][j] == 4:
                    if 0 <= i < N and 0 <= j + 1 < M:
                        if data[i][j + 1] == 1 or data[i][j + 1] == 3 or data[i][j + 1] == 6 or data[i][j + 1] == 7:
                            maze[2*i][2*j + 1] = 1

                elif data[i][j] == 5:
                    if 0 <= i < N and 0 <= j + 1 < M:
                        if data[i][j + 1] == 1 or data[i][j + 1] == 3 or data[i][j + 1] == 6 or data[i][j + 1] == 7:
                            maze[2 * i][2 * j + 1] = 1
                    if 0 <= i + 1 < N and 0 <= j < M:
                        if data[i+1][j] == 1 or data[i+1][j] == 2 or data[i+1][j] == 4 or data[i+1][j] == 7:
                            maze[2*i+1][2*j] = 1

                elif data[i][j] == 6:
                    if 0 <= i+1 < N and 0 <= j < M:
                        if data[i+1][j] == 1 or data[i+1][j] == 2 or data[i+1][j] == 4 or data[i+1][j] == 7:
                            maze[2*i+1][2*j] = 1


    # 맨홀 뚜껑
    stack = []
    stack.append((2*R, 2*C))
    visited = [[0]*2*M for _ in range(2*N)]

    visited[2*R][2*C] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while stack:

        # if count == 2*L:
        #     break

        y, x = stack.pop(0)

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= nx < 2*M and 0 <= ny < 2*N:
                if maze[ny][nx] >= 1:
                    if visited[ny][nx] == 0:
                        stack.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1
                        if visited[y][x] + 1 > 3 * L:
                            break


    cnt = 0
    for i in range(2*N):
        for j in range(2*M):
            if 0 < visited[i][j] < 2*L:
                if visited[i][j] % 2:
                    cnt += 1
    print(f'#{tc}', cnt)

