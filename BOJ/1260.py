import sys

input = sys.stdin.readline

def DFS(x):

    q = []
    visited = [False] * (n + 1)

    q.append(x)
    # visited[x] = True

    while q:

        now = q.pop()

        if visited[now]:
            continue

        visited[now] = True
        print(now, end=" ")

        for next in sorted(data[now], reverse=True):
            if not visited[next]:
                # visited[next] = True
                q.append(next)


def BFS(x):

    q = []
    visited = [False] * (n + 1)

    q.append(x)
    visited[x] = True

    while q:

        now = q.pop(0)
        print(now, end=" ")

        for next in sorted(data[now]):
            if not visited[next]:
                visited[next] = True
                q.append(next)

n, m, v = map(int, input().split())

data = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    data[n1].append(n2)
    data[n2].append(n1)

DFS(v)
print()
BFS(v)
