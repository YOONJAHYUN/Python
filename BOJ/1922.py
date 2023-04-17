import sys
input = sys.stdin.readline

def find(start):

    if start != vroot[start]:
        vroot[start] = find(vroot[start])
    return vroot[start]


# 컴퓨터의 수
n = int(input())
# 연결할 수 있는 선의 수
m = int(input())

graph = []
vroot = [i for i in range(n+1)]
# 컴퓨터 연결하는데 드는 비용
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
ans = 0
for cost, a, b in graph:

    aa = find(a)
    bb = find(b)

    if aa != bb:

        if aa > bb:
            vroot[aa] = bb
        else:
            vroot[bb] = aa
        ans += cost
print(ans)