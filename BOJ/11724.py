import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
node = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

q = []
visited = [0] * (N+1)

q.append(1)
visited[1] = 1

def f(n):

    while q:

        dot = q.pop()

        for i in node[dot]:
            if visited[i] == 0:
                visited[i] = n
                q.append(i)


    for i in range(1, N+1):
        if visited[i] == 0:
            q.append(i)
            f(n+1)


f(1)

print(max(visited))