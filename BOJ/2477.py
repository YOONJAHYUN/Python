import sys

input = sys.stdin.readline

# 참외의 개수
K = int(input())

data = []

for _ in range(6):
    a, b = map(int, input().split())
    data.append((a, b))

max_12 = 0
max_12_idx = 0

max_34 = 0
max_34_idx = 0

for i in range(6):
    if data[i][0] == 1 or data[i][0] == 2:
        if max_12 < data[i][1]:
            max_12 = data[i][1]
            max_12_idx = i
    else:
        if max_34 < data[i][1]:
            max_34 = data[i][1]
            max_34_idx = i

index_list = [data[max_34-1], data[(max_34+1)%6], data[max_12-1], data[(max_12-1)%6]]
print(index_list)