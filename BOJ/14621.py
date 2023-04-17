import sys
input = sys.stdin.readline

def find(start):
    if start != vroot[start]:
        vroot[start] = find(vroot[start])
    return vroot[start]

# n 학교의 수 m 도로의 개수
n, m = map(int, input().split())

school = [0] + input().split()
check = [True] + [False for _ in range(n)]
# print(check)
graph = []
vroot = [i for i in range(n+1)]
for _ in range(m):
    u, v, d = map(int, input().split())
    graph.append((d, u, v))

graph.sort()
ans = 0
for d, u, v in graph:
    if school[u] != school[v]:
        uu = find(u)
        vv = find(v)

        if uu != vv:
            if uu > vv:
                vroot[uu] = vv
            else:
                vroot[vv] = uu

            check[u], check[v] = True, True

            ans += d
# print(check)

for val in check:
    if not val:
        print(-1)
        break
else:
    print(ans)
