import sys

sys.stdin = open('input.txt')

def rec(sx, sy, gx, gy, visited):
    global result, q
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if sx == gx and sy == gy:
        result = 1
        return result

    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]

        if 0 <= nx < 16 and 0 <= ny < 16:
            if mat[ny][nx] == 0:
                if visited[ny][nx] == 0:
                    q.append((nx, ny))

            elif mat[ny][nx] == 3:
                result = 1
                return
    if q:
        sx, sy = q.pop(0)
        visited[sy][sx] = 1
        rec(sx, sy, gx, gy, visited)

    else:
        return


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

    q.append((start_x, start_y))
    visited[start_y][start_x] = 1
    result = 0
    rec(start_x, start_y, goal_x, goal_y, visited)

    print(f'#{tc}', result)
