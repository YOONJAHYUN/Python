import sys

sys.stdin = open('input.txt')

T = int(input())

def room_route():
    global cnt

    while stack:
        x, y = stack.pop()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if rooms[ny][nx] == rooms[y][x] + 1:
                    stack.append((nx, ny))


    if not stack:
        if rooms[y][x] == N:
            result.append(cnt)

        else:
            for i in range(N):
                for j in range(N):
                    if rooms[i][j] == rooms[y][x]+1:
                        stack.append((j, i))
                        result.append(cnt)
                        cnt = 1
                        room_route()



for tc in range(1, T+1):
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    stack = []
    cnt = 1
    result = []

    for i in range(N):
        for j in range(N):
            if rooms[i][j] == 1:
                stack.append((j, i))


    room_route()
    print(result)
