import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]

# print(maze)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

stack = deque()
stack.append((0, 0))
visited = [[0]*M for _ in range(N)]
# print(visited)
visited[0][0] = 1

while stack:

    x, y = stack.popleft()

    if x == M-1 and y == N-1:
        print(visited[y][x])
        break

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y

        if 0 <= nx < M and 0 <= ny < N:
            if maze[ny][nx] == 1:
                if visited[ny][nx] == 0:
                    stack.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1




