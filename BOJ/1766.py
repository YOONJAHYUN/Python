import sys
from heapq import heappop, heappush
# from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = []
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(q, i)

    while q:
        now = heappop(q)
        result.append(now)

        for next_node in graph[now]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                heappush(q, next_node)

    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(* topology_sort())
