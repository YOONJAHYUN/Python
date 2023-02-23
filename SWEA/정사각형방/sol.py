import sys

sys.stdin = open('input.txt')

def room_route(count, x, y, n):
    global cnt, result

    visited[y][x] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if rooms[ny][nx] == rooms[y][x] + 1:

                x = nx
                y = ny

                cnt += 1

                room_route(count+1, x, y, n)


    else:
        for i in range(n):
            for j in range(n):
                # if visited[i][j] == 0:
                result.append(cnt)
                cnt = 1
                start.append(rooms[i][j])
                room_route(1, j, i, n)




T = int(input())

for tc in range(1, T+1):
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 1
    result = []
    start = []
    start.append(rooms[0][0])
    visited = [[0]* N for _ in range(N)]

    room_route(1, 0, 0, N)

    ans = max(result)
    # for i in

    print('start', start)
    print('결과', result)
    print(ans)



