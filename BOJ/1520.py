import sys

input = sys.stdin.readline

def dfs(y, x):
    # 방문하지 않은 경우에만 들어옴
    if visited[y][x] == -1:

        visited[y][x] = 0

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny = y + dy
            nx = x + dx

            if data[y][x] < data[ny][nx]:
                visited[y][x] += dfs(ny,nx)
    return visited[y][x]

m, n = map(int, input().split())
data = [[0]*(n+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(m)] + [[0]*(n+2)]

# 갈 수 있는 곳을 먼저 체크해보자
visited = [[-1]*(n+2) for _ in range(m+2)]
visited[1][1] = 1

print(dfs(m,n))

