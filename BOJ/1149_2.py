import sys

input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# R은 이전 값의 G or B 중 더 작은 것을 합하여 와야함.
for i in range(1, N):
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

print(min(data[N-1]))






