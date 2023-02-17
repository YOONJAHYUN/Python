import sys

input = sys.stdin.readline


N, M, R = map(int, input().split())

node = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

# print(node)
stack = []
stack.append(R)
visited = [0] * (N+1)
cnt = 1

while stack:

    R = stack.pop()

    if not visited[R]:
        visited[R] = cnt
        cnt += 1

    for i in sorted(node[R], reverse=True):
        if not visited[i]:
            stack.append(i)

# print(*visited[1:])
for i in range(1, N+1):
    print(visited[i])