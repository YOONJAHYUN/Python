import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0]*(k+1)
dp[0] = 1
# dp = [[0]*(k+1) for _ in range(n+1)]
coin = [int(input()) for _ in range(n)]

for i in range(1, n+1):
    money = coin[i-1]
    for j in range(k+1):
        if j >= money:
            dp[j] = dp[j] + dp[j-money]
print(dp[-1])
