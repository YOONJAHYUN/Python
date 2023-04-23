import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[int(1e9)]*(k+1) for _ in range(n)]

for i in range(n):
    coin = int(input())
    dp[i][0] = 0
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-coin]+1)
        else:
            dp[i][j] = dp[i - 1][j]
ans = dp[n-1][-1]

if ans == int(1e9):
    print(-1)
else:
    print(ans)