import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

jump = [[0]*N for _ in range(N)]

jump[0][0] = 1

for i in range(N):
    for j in range(N):
        if data[i][j] == 0:
            continue
        if 0 <= j + data[i][j] < N:
            jump[i][j+data[i][j]] += jump[i][j]
        if 0 <= i + data[i][j] < N:
            jump[i + data[i][j]][j] += jump[i][j]

# for i in jump:
#     print(i)
print(jump[-1][-1])
