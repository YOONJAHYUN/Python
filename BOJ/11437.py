import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# A와 B의 최소 공통 조상을 찾는 함수
def LCA(a, b):
    # 깊이가 동일하도록 만들어 준다.
    while d[a] != d[b]:

        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

# 루트 노드부터 시작해 깊이(depth)를 구하는 함수
def DFS(x, depth):
    c[x] = True
    d[x] = depth

    for y in graph[x]:
        # 이미 깊이를 구했다면 넘기기
        if c[y]:
            continue
        parent[y] = x
        DFS(y, depth+1)

n = int(input())

# 부모 노드 정보
parent = [0] * (n+1)

# 각 노드까지의 깊이
d = [0] * (n+1)

# 각 노드의 깊이가 계산되었는지 여부
c = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드는 1번 노드
DFS(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))