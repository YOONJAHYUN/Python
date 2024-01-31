import sys

input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a>b:
        a,b = b,a

    parent[b] = a


n, m, k = map(int, input().split())

edge = []

for i in range(1, 1+m):
    x, y = map(int, input().split())
    edge.append((x, y, i))

for i in range(k):
    ans = 0
    parent = list(range(n+1))

    for x, y, w in edge:

        if find(x) != find(y):
            union(x, y)
            ans += w

    for j in range(1, n+1):
        if find(j) != 1:
            print(0, end=" ")
            break
    else:
        print(ans, end=" ")
    edge.pop(0)

