import sys

input = sys.stdin.readline

# 대표원소 정리
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

edge = []

for i in range(n):
    for j in range(i+1, n):
        edge.append((data[i][j], i, j))
        edge.append((data[i][j], j, i))


edge.sort()
parent = list(range(n+1))

result = 0

for w, s, e in edge:
    if find_set(s) != find_set(e):
        union(s, e)
        result += w
print(result)


