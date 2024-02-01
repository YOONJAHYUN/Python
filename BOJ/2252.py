import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for nnext in graph[now]:
            indegree[nnext] -= 1

            if not indegree[nnext]:
                q.append(nnext)

    for i in result:
        print(i, end=' ')


n, m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()



