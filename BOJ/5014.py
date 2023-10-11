import sys
input = sys.stdin.readline
from collections import deque


F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)

def BFS(x):


    q = deque()

    q.append((x, 0))
    visited[x] = True

    while q:

        now, step = q.popleft()

        if now == G:
            print(step)
            break

        if 0 < now + U <= F and not visited[now+U]:
            visited[now+U] = True
            q.append((now+U, step+1))

        if 0 < now - D <= F  and not visited[now-D]:
            visited[now-D] = True
            q.append((now-D, step+1))

    else:
        print("use the stairs")


BFS(S)