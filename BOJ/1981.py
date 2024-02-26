import sys
from collections import deque
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[(201, 201, -1)] * n for _ in range(n)]

q = deque()
q.append((0, 0, arr[0][0], arr[0][0]))
# visited[0][0] = (min(arr[0][0], 201), max(arr[0][0], -1))
answer = 201

'''
5
3 4 11 8 7 
0 12 17 11 10 
13 19 12 15 6 
10 8 15 17 18 
6 0 15 1 8 

answer= 14
'''


while q:

    y, x, max_count, min_count = q.popleft()

    if y == n-1 and x == n-1:
        answer = min(answer, max_count-min_count)
        continue

    for k in range(4):
        dy, dx = DIR[k][0], DIR[k][1]
        ny, nx = y+dy, x+dx

        if 0 <= ny < n and 0 <= nx < n and (visited[ny][nx][1] > max_count or visited[ny][nx][2] < min_count):
            visited[ny][nx] = (min(max_count, visited[ny][nx][0]), max(min_count, visited[ny][nx][1]))
            q.append((ny, nx, max(max_count, arr[ny][nx]), min(min_count, arr[ny][nx])))

for i in visited:
    print(i)

print(answer)





