import sys

input = sys.stdin.readline

# 시간복잡도 : n**3

n = int(input())

my_dict = {}
data = []
for _ in range(n):
    temp = int(input())
    my_dict[temp] = 1
    data.append(temp)

data.sort()

ans = 0

for i in range(n-2, -1, -1):
    for j in range(i, -1, -1):
        for k in range(j, -1, -1):
            tmp = data[i] + data[j] + data[k]
            if my_dict.get(tmp):
                ans = max(tmp, ans)

print(ans)

