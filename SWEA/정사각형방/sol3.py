import sys

sys.stdin = open('input.txt')

def room_route(x, y):
    global cnt, check, start

    if rooms[y][x] == N * N:
        result.append(cnt)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if rooms[ny][nx] == rooms[y][x] + 1:
                x = nx
                y = ny

                cnt += 1
                check[rooms[ny][nx]] = True

                room_route(x, y)

    else:

        for idx in range(1+N*N):
            if check[idx] == False:
                for i in range(N):
                    for j in range(N):
                        if rooms[i][j] == idx:
                            x, y = j, i
                            check[rooms[y][x]] = True
                            result.append(cnt)
                            cnt = 1
                            start.append(rooms[y][x])

                            room_route(x, y)
                            return

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    check = [False for _ in range(N*N+1)]
    cnt = 1
    result = []
    start = []

    for i in range(N):
        for j in range(N):
            if rooms[i][j] == 1:
                x, y = j, i
                break
    check[1] = True
    start.append(rooms[y][x])
    room_route(x, y)

    print('result', result)
    print('start', start)
    print('##################')