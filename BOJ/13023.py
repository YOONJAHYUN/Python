import sys
input = sys.stdin.readline

def DFS(now, cnt):
    if cnt == 4:
        print(1)
        exit(0)

    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            DFS(next_node, cnt+1)
            visited[next_node] = False


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

for i in range(n):
    visited[i] = True
    DFS(i, 1)
    visited[i] = False

print(0)