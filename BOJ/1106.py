import sys
input = sys.stdin.readline

# 고객을 적어도 C명 늘려야됨
# 홍보할 수 있는 도시의 개수 N
C, N = map(int, input().split())

dp = [[1e9] * (C+1) for _ in range(N+1)]

data = [(0,0)]
for _ in range(N):
    cost, customer = map(int, input().split())
    data.append((cost, customer))

for i in range(1, N+1):
    cost, customer = data[i]

    for j in range(1, C+1, cost):

        if j < customer:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-customer]+cost)

    for i in dp:
        print(i)
    print()
print(dp[N][C])
