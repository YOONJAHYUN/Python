import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001
q = deque()

q.append((N, 0))
visited[N] = 1

while True:

    x, time = q.popleft()

    if x == K:
        print(time)
        break

    if 0 <= x*2 <= 100000 and not visited[x*2]:
        q.append((x * 2, time))
        visited[x*2] = 1

    if 0 <= x-1 <= 100000 and not visited[x-1]:
        q.append((x - 1, time + 1))
        visited[x-1] = 1

    if 0 <= x+1 <= 100000 and not visited[x+1]:
        q.append((x + 1, time + 1))
        visited[x+1] = 1
