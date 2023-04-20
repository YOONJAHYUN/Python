import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 루트 있으면 1 없으면 0, 안지나갓음 -1
check = [[-1] * n for _ in range(n)]

my_min = 1e9
min_index = (0, 0)
for i in range(n):
    for j in range(n):
        if i!=j and graph[i][j] < my_min:
            my_min = graph[i][j]
            min_index = (i, j)
# 최저를 구하고 그 인덱스를 활용한다.
print(min_index)
y, x = min_index

check[y][x] = 1
# 거기서의 최저를 구함
my_min2 = 1e9
min2_index = (0,0)
for i in range(n):
    if x != i and graph[x][i] < my_min2:
        my_min2 = graph[x][i]
        min2_index = (x, i)
x, m = min2_index
# min1에서 min2까지 갈 수 있는지 체크
if graph[x][m] + graph[m][y] == graph[x][y]:
    check[x][y] = 1
    check[y][x] = 1
else:
    check[x][y] = 0
    check[y][x] = 0

for i in check:
    print(i)

