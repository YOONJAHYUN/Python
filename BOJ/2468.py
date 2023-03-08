import sys
import copy

input = sys.stdin.readline

def finding(num):
    map = copy.deepcopy(data)

    for i in range(N):
        for j in range(N):
            if map[i][j] <= num:
                map[i][j] = 0

    visited = [[False]*N for _ in range(N)]
    stack = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if map[i][j] and not visited[i][j]:
                stack.append((i,j))
                cnt += 1
                visited[i][j] = True
                while stack:
                    ni, nj = stack.pop()

                    for di, dj in ((1,0), (-1, 0), (0,1), (0,-1)):
                        si, sj = ni + di, nj + dj

                        if 0 <= si < N and 0 <= sj < N and map[si][sj] and not visited[si][sj]:
                            stack.append((si, sj))
                            visited[si][sj] = True
    return cnt







N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

height = []

for i in range(N):
    for j in range(N):
        if data[i][j] not in height:
            height.append(data[i][j])
total = 1
for h in height:
    num = finding(h)
    total = max(total, num)

print(total)
