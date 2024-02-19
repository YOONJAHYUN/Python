import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    lst = list(map(int, input().split()))
    for i in range(1, lst[0]):
        graph[lst[i]].append(lst[i+1])
        indegree[lst[i+1]] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    now = q.popleft()
    result.append(now)
    for next_node in graph[now]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)
