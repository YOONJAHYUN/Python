import sys
# from collections import deque
input = sys.stdin.readline

N = int(input())

node = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c = map(int, input().split())
    node[c].append(p)
    node[p].append(c)
# print(node)
tree = [0] * (N+1)
# print(tree)

root = 1
stack = []
stack.append(1)
visited = [False for _ in range(N+1)]
visited[1] = True

while True:

    while stack:
        root = stack.pop()

        for i in node[root]:
            if visited[i] == False:
                visited[i] = True
                tree[i] = root
                stack.append(i)
                # print(tree)

    if not stack and visited.count(False) == 1:
        for i in tree[2:N+1]:
            print(i)
        break

    if not stack:
        for i in range(2, N+1):
            if visited[i] == False:
                stack.append(i)






