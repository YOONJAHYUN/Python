import sys

sys.stdin =open('input.txt')

def love_maze():

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if maze[ny][nx] == 0:
                if visited[ny][nx] == 0:
                    stack.append((nx, ny))
                    visited[ny][nx] = 1

            elif maze[ny][nx] == 3:

                return 1
    else:
        return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input().rstrip())) for _ in range(100)]

    visited = [[0]*100 for _ in range(100)]
    stack = []
    stack.append((1, 1))
    visited[1][1] = 1
    print(f'#{tc}', love_maze())


