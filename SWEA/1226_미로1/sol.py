import sys

sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())

    mat = [list(map(int, input().rstrip())) for _ in range(16)]

    # 시작점 찾기, 도착점 찾기
    for i in range(16):
        for j in range(16):
            if mat[i][j] == 2:
                start_x, start_y = j, i
            elif mat[i][j] == 3:
                goal_x, goal_y = j, i

    visited = [[0] * 16 for _ in range(16)]
    q = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q.append((start_x, start_y))
    visited[start_y][start_x] = 1

    x = start_x
    y = start_y

    result = 0

    while q and result != 1:
        x, y = q.pop(0)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if mat[ny][nx] == 0:
                    if visited[ny][nx] == 0:
                        q.append((nx, ny))
                        visited[ny][nx] = 1

                elif mat[ny][nx] == 3:
                    print(f'#{tc}', 1)
                    result = 1
                    break

    print(f'#{tc}', result)
