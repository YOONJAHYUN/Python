import sys

input = sys.stdin.readline

def jelly():
    while stack:
        nx, ny = stack.pop()

        dx = [0, 1]
        dy = [1, 0]
        jump = map[ny][nx]
        for k in range(2):

            sx = nx + dx[k] * jump
            sy = ny + dy[k] * jump

            if 0 <= sx < N and 0 <= sy < N:
                    if map[sy][sx] == -1:
                        print('HaruHaru')
                        return

                    else:
                        if 1<= map[sy][sx] <=5:
                            stack.append((sx, sy))
    else:
        print("Hing")
        return

N = int(input())

map = [list(map(int, input().split())) for _ in range(N)]
# start 지점
x, y = 0, 0

stack = []
stack.append((x, y))

jelly()
