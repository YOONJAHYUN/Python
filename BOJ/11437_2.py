import sys
from collections import deque
input = sys.stdin.readline

# depth level 체크 함수
def BFS(num):

    q = deque()
    q.append((num, 0))

    while q:
        x, depth = q.popleft()
        d[x] = depth
        v[x] = True

        for y in graph[x]:
            # 방문하지 않았다면
            if not v[y]:
                v[y] = True
                parent[y] = x
                q.append((y, depth+1))

# 공통 조상 찾기
def LCA(a, b):

    # a와 b level을 맞춘다.
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # level을 맞춘 후, 하나씩 올라가면서 조상찾기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

n = int(input())

graph = [[] for _ in range(n+1)]

d = [0] * (n+1)
parent = [0] * (n+1)
v = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트가 1, 각자 depth level 저장
BFS(1)
print(d)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))