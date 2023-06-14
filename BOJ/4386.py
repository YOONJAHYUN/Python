def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)


n = int(input())

parent = [i for i in range(n+1)]

star = [(0, 0)] * (n+1)

edge = []

result = 0

for i in range(1, n+1):
    x, y = map(float, input().split())
    star[i] = x, y


for i in range(1, n+1):
    for j in range(i+1, n+1):
        distance = ((star[j][0] - star[i][0]) ** 2 + (star[j][1] - star[i][1]) ** 2) ** 0.5
        edge.append((distance, i, j))

edge.sort()

for dis, a, b in edge:
    if find_set(a) != find_set(b):
        union(a, b)
        result += dis
print(round(result, 2))
