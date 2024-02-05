import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():

    res = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            res[i] = times[i-1]

    while q:

        now = q.popleft()

        if now == w:
            print(res[now])
            return

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

            res[i] = max(res[i], res[now] + times[i-1])

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(k):
        x, y = map(int, input().split())

        graph[x].append(y)
        indegree[y] += 1

    w = int(input())
    topology_sort()

