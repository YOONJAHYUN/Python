import sys
input = sys.stdin.readline

def find(start):

    if start != vroot[start]:
        vroot[start] = find(vroot[start])
    return vroot[start]

n, m = map(int, input().split())

graph = []
for _ in range(m+1):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

vroot = [i for i in range(n+1)]

ans = 0
ans2 = 0
for energy, a, b in graph:
    aa = find(a)
    bb = find(b)

    if aa != bb:
        if aa > bb:
            vroot[aa] = bb
        else:
            vroot[bb] = aa

        if energy == 0:
            ans += 1

graph.sort(key=lambda x:-x[0])

vroot = [i for i in range(n+1)]
for energy, a, b in graph:
    aa = find(a)
    bb = find(b)

    if aa != bb:
        if aa > bb:
            vroot[aa] = bb
        else:
            vroot[bb] = aa

        if energy == 0:
            ans2 += 1

# print(ans)
# print(ans2)
print(ans**2 - ans2**2)
