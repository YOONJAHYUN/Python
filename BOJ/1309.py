import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * (n+1) for _ in range(2)]
dp[1][0] = 1
dp[1][1] = 2

for j in range(1, n+1):
    dp[0][j] = dp[0][j-1] + dp[1][j-1]
    dp[1][j] = dp[0][j-1]*2 + dp[1][j-1]

ans = dp[0][n] + dp[1][n]
# print(dp)
print(ans)
