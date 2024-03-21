import sys
from collections import deque
input = sys.stdin.readline

def gravity():
    global arr
    for j in range(n):
        for i in range(1, n):

            if arr[i][j] == -2:
                now_y = i

                while now_y > 0:
                    if arr[now_y-1][j] == -1:
                        break
                    arr[now_y][j], arr[now_y-1][j] = arr[now_y-1][j], arr[now_y][j]
                    now_y -= 1

# 격자 한 변의 크기 n, 색상의 개수 m
# 검 -1 무지개 0
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
while True:

    group = []
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            q = deque()
            color = 0
            cnt = 0
            rainbow = 0
            if not visited[i][j] and arr[i][j] > 0:
                q.append((i, j))
                visited[i][j] = True
                color = arr[i][j]

                while q:
                    y, x = q.popleft()
                    cnt += 1

                    for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] >= 0:
                            # 무지개 색일 경우
                            if arr[ny][nx] == 0 and not visited[ny][nx]:
                                q.append((ny, nx))
                                visited[ny][nx] = True
                                rainbow += 1
                            # 같은 컬러인 경우
                            elif not visited[ny][nx] and arr[ny][nx] == color:
                                visited[ny][nx] = True
                                q.append((ny, nx))

                if cnt < 2:
                    continue

                for iii in range(n):
                    for jjj in range(n):
                        if arr[iii][jjj] == 0:
                            visited[iii][jjj] = False

                group.append((cnt, rainbow, i, j))
    group.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))

    if len(group) == 0:
        break

    # 그룹의 모든 블록을 제거한다.
    count, rainbow2, ii, jj = group[0]
    answer += count ** 2

    new_q = deque()
    new_q.append((ii, jj))
    new_color = arr[ii][jj]
    new_visited = [[False] * n for _ in range(n)]
    new_visited[ii][jj] = True

    while new_q:
        yy, xx = new_q.popleft()
        arr[yy][xx] = -2

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = yy + dy, xx + dx
            if 0 <= ny < n and 0 <= nx < n and (arr[ny][nx] == 0 or arr[ny][nx] == new_color) and not new_visited[ny][nx]:
                new_q.append((ny, nx))
                new_visited[ny][nx] = True

    # 중력 작용
    gravity()

    arr = list(reversed(list(map(list, zip(*arr)))))

    # 중력 작용
    gravity()

print(answer)
