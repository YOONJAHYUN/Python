import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def BFS(lst):
    # global virus
    cnt = 0
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for y, x in wall:
        visited[y][x] = '-'
    # print(lst)
    for y, x in lst:
        q.append((y, x))
        visited[y][x] = 0
    while q:
        y, x = q. popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and data[ny][nx] != 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
                cnt = max(cnt, visited[ny][nx])

    for line in visited:
    #     print(line)

        if -1 in line:
            return
    else:
        return cnt
    # for i in range(N):
    #     for j in range(N):
    #         if visited[i][j] == -1:
    #             return my_max
    #         else:
    #             my_max = max(my_max, visited[i][j])
    # return my_max






# 순열 선택
def location(depth, n, ans):
    global result
    if depth == n:
        if len(ans) == M:
            if BFS(ans) != None:
                result.append(BFS(ans))
            # print(BFS(ans))
        return
    #포함하는 경우
    location(depth+1, n, ans+[virus[depth]])
    #포함하지 않는경우
    location(depth+1, n, ans)


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

'''
바이러스는 상하좌우 복제
0 빈칸
1 벽
2 바이러스를 놓을 수 있는 칸

모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간
'''

virus = []
wall = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
          virus.append((i,j))
        elif data[i][j] == 1:
            wall.append((i,j))
n = len(virus)

result = []
location(0, n, [])
if result:
    print(min(result))
else:
    print(-1)

'''
바이러스를 놓을 수 있는 칸 들 중에서 몇개를 선택할건지 고른다
-> 순열

이후 bfs를 사용해서 감염경로 중 가장 짧은 걸 고른다.

5 2
1 1 1 1 1
1 1 2 1 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1
'''



