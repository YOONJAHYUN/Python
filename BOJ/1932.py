import sys
input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
if n >= 2:
    data[1][0] += data[0][0]
    data[1][1] += data[0][0]


    for i in range(2, n):
        for j in range(i+1):
            if j >= 1 and j<i:
                data[i][j] += max(data[i-1][j-1], data[i-1][j])
            elif j==0:
                data[i][j] += data[i-1][j]
            else:
                data[i][j] += data[i-1][j-1]
    print(max(data[-1]))
else:
    print(*data[0])