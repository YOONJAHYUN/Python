import sys
input = sys.stdin.readline

def find(start):
    if start != vroot[start]:
        vroot[start] = find(vroot[start])
    return vroot[start]


# 집의 개수 n 길의 개수 m
n, m = map(int, input().split())
vroot = [i for i in range(n+1)]
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

ans = 0
final = 0
for cost, a, b in graph:

    aa = find(a)
    bb = find(b)
    if aa != bb:
        if aa > bb:
            vroot[aa] = bb
        else:
            vroot[bb] = aa
        final = cost
        ans += cost

print(ans-final)
