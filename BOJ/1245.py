import sys
input = sys.stdin.readline

def DFS(y, x):

    check = True

    q = []
    q.append((y, x))

    visited[y][x] = True

    while q:

        y, x = q.pop()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            ny, nx = y + dy, x + dx

            if 0 <= nx < m and 0 <= ny < n:

                if not visited[ny][nx] and data[ny][nx] == data[y][x]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

                elif data[ny][nx] > data[y][x]:
                    check = False
    if check:
        return True
    return False


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]


count = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):

        if not visited[i][j] and DFS(i, j):
            count += 1

print(count)
