import sys

input = sys.stdin.readline

n = int(input())

data = [[int(1e9)]*(n+1) for _ in range(n+1)]
while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    data[a][b] = 1
    data[b][a] = 1

# for i in range(n+1):
#     data[i][i] = 0


# 플로이드 워셜
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # 이미 친구거나 내 자신인 경우는 제외
            if data[j][k] == 1 or data[j][k] == 0:
                continue
            elif data[j][k] > data[j][i] + data[i][k]:
                data[j][k] = data[j][i] + data[i][k]

for i in range(n+1):
    data[i][i] = 0

# for i in data:
#     print(i)
ans = 1e9
res = []
for i in range(1, n+1):
    if max(data[i][1:]) < ans:
        ans = max(data[i][1:])
        res = [i]
    elif max(data[i][1:]) == ans:
        res.append(i)

print(ans, len(res))
print(*res)

