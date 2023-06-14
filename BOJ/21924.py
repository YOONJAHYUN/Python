import sys

input = sys.stdin.readline

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

n, m = map(int, input().split())

data = []
total = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))
    total += cost

data.sort()

parent = [i for i in range(n+1)]
result = 0

for w, s, e in data:
    ss = find_set(s)
    ee = find_set(e)

    if ss != ee:

        if ss > ee:
            parent[ss] = ee
        else:
            parent[ee] = ss

        result += w

print(parent)

print(total - result)


