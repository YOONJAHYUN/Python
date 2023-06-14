import sys

input = sys.stdin.readline

def find(x):
    if x != vroot[x]:
        vroot[x] = find(vroot[x])
    return vroot[x]

while True:
    m,n = map(int, input().split())
    if m == 0 and n == 0:
        break

    graph = []
    result = 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
        result += c

    graph.sort()

    vroot = [i for i in range(m+1)]

    ans = 0

    for dist, a, b in graph:
        aa = find(a)
        bb = find(b)

        if aa != bb:
            if aa > bb:
                vroot[aa] = bb
            else:
                vroot[bb] = aa
            ans += dist

    print(result - ans)
