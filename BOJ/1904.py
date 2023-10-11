import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 2
if n > 1:
    for i in range(2, n):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n-1])
