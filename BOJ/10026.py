import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())

data1 = [list(input().rstrip()) for _ in range(N)]
data2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data1[i][j] == 'G':
            data2[i][j] = 'R'
        else:
            data2[i][j] = data1[i][j]



visited1 = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
# 적록색약이 아닌 사람은 RGB 구분가능
# 적록색약은 RG 같고, B다름

# 적록색약이 아닌 사람
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

x, y = 0, 0

stack = []


# 재귀로 풀어보자
def color(a, b, number, data, visited):

    stack.append((a, b))
    visited[b][a] = number

    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if data[y][x] == data[ny][nx] and visited[ny][nx] == 0:
                    visited[ny][nx] = number
                    stack.append((nx, ny))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                color(j, i, number+1, data, visited)
                return

color(0, 0, 1, data1, visited1)
color(0, 0, 1, data2, visited2)
my_max1 = 0
my_max2 = 0
for i in range(N):
    for j in range(N):
        my_max1 = max(visited1[i][j], my_max1)
        my_max2 = max(visited2[i][j], my_max2)
print(my_max1, my_max2)
