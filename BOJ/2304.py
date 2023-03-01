import sys

input = sys.stdin.readline

N = int(input())
data = [0] * 1002
line = [0] * 1002
for _ in range(N):
    L, H = map(int, input().split())
    data[L] = H

my_max = max(data)
max_index = []

for i in range(1002):
    if data[i] == my_max:
        max_index.append(i)

for i in range(1, 1002):
    # 최댓값 직전
    if i <= max_index[0]:
        if line[i-1] > data[i]:
            line[i] = line[i - 1]
        else:
            line[i] = data[i]

# 최댓값 이후 -> 뒤집기
for i in range(1000, max_index[0], -1):

    if data[i] < line[i+1]:
        line[i] = line[i+1]
    else:
        line[i] = data[i]

print(sum(line))

