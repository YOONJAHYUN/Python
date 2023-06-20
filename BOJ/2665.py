import sys
from collections import deque
input = sys.stdin.readline

def BFS(y, x):

    q = deque()
    q.append((0, y, x))

    while q:
        cnt, sy, sx = q.popleft()

        if sy == n-1 and sx == n-1:
            print(cnt)
            return

        if visited[sy][sx] < cnt:
            continue

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = sy+dy, sx+dx

            if 0 <= ny < n and 0 <= nx < n:
                # print(ny, nx)
                # 문자열로 받았으니까 문자열로 하기
                if rooms[ny][nx] == '0':
                    if visited[ny][nx] > cnt + 1:
                        visited[ny][nx] = cnt + 1
                        q.append((cnt+1, ny, nx))
                else:
                    if visited[ny][nx] > cnt:
                        visited[ny][nx] = cnt
                        q.appendleft((cnt, ny, nx))



n = int(input())
rooms = [input().rstrip() for _ in range(n)]
# print(rooms)
visited = [[int(1e9)] * n for _ in range(n)]

BFS(0, 0)