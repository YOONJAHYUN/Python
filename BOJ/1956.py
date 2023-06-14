import sys

input = sys.stdin.readline

v, e = map(int, input().split())
data = [[int(1e9)] * (v+1) for _ in range(v+1)]


# print(data)
for _ in range(e):
    a, b, c = map(int, input().split())
    data[a][b] = c


for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            data[j][k] = min(data[j][i] + data[i][k], data[j][k])

ans = int(1e9)
for i in range(1, v+1):
    ans = min(ans, data[i][i])

if ans == int(1e9):
    print(-1)
else:
    print(ans)
