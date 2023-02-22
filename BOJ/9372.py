import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())

    node = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        node[a].append(b)
        node[b].append(a)

    q = deque()
    q.append(1)
    visited = [-1] * (N+1)
    visited[1] = 0
    cnt = 0
    while q:

        country = q.popleft()

        for i in node[country]:
            if visited[i] == -1:
                visited[i] = visited[country] + 1
                q.append(i)
                cnt += 1


    print(cnt)