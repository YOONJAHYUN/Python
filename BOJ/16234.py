import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

# print(visited[1][1])

dy = [0,1,0,-1]
dx = [1,0,-1, 0]
cnt = 0

q = deque()
while True:
    new_country = [[0]*N for _ in range(N)]

    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                q.append([i,j])
                check = []

                while q:
                    y, x = q.popleft()
                    check.append([y,x])
                    person = country[y][x]
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[ny][nx] and L <= abs(country[ny][nx] - person) <= R:
                                visited[ny][nx] = True
                                q.append([ny, nx])

                people = 0

                for sy, sx in check:
                    people += country[sy][sx]

                new = int(people/len(check))
                for sy, sx in check:
                    new_country[sy][sx] = new

    if new_country == country:
        break
    else:
        cnt += 1
        country = new_country
    # cnt += 1
    #     for i in country:
        #     print(i)
        # print()

    # break


    # if new

    # for i in country:
    #     print(i)


print(cnt)

