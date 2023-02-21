import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().rstrip())) for _ in range(N)]

    # print(mat)
    # 0은 통로, 1은 벽, 2는 출발, 3은 도착

    # 출발지 index찾기
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                x, y = j, i

    # print(x, y)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = []
    visited = [[0]*N for _ in range(N)]
    q.append((x, y))
    visited[y][x] = 0
    # print(q)
    # print(visited)

    while q:
        a, b = q.pop(0)
        for k in range(4):

            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < N and 0 <= ny < N:

                if mat[ny][nx] == 0:
                    if visited[ny][nx] == 0:
                        q.append((nx, ny))
                        visited[ny][nx] = visited[b][a] + 1

                elif mat[ny][nx] == 3:
                    visited[ny][nx] = visited[b][a]
                    break
    # for i in visited:
    #     print(i)
    # print(visited)
    # 도착점 index
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 3:
                final_y, final_x = i, j

    print(f'#{tc}', visited[final_y][final_x])