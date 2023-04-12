import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 10001
# dp = [0, 1, 3, 5, 11] + [0]*500

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1

    elif i == 2:
        dp[i] = 3

    elif i == 3:
        dp[i] = 5

    elif i == 4:
        dp[i] = 11

    else:

        dp[i] = (dp[i-2]*2 + dp[i-1])%10007

print(dp[n])