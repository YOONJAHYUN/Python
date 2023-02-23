import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]


    for i in range(N):
        for j in range(N):
            if rooms[i][j] == 1:
                startx = j
                starty = i
                break



    stack = []
    stack.append((startx, starty))
    visited = [[0] * N for _ in range(N)]

    visited[starty][startx] = 1

    while stack:
        while stack:
            x, y = stack.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    if rooms[ny][nx] == rooms[y][x] + 1 or rooms[ny][nx] == rooms[y][x] - 1:
                        if visited[ny][nx] == 0:
                            stack.append((nx, ny))
                            visited[ny][nx] = visited[y][x] + 1

        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    stack.append((j, i))
                    visited[i][j] = 1
                    break
                break
    print(visited)
    my_max = 1
    ans = N*N
    for i in range(N):
        for j in range(N):
            my_max = max(visited[i][j], my_max)

    for i in range(N):
        for j in range(N):
            if my_max == visited[i][j]:
                ans = min(rooms[i][j]-my_max+1, ans)

    print(f'#{tc}', ans, my_max)



