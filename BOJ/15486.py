import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]


for i in range(1, n+1):

    t, p = map(int, input().split())

    day = t + i - 1

    dp[i] = max(dp[i], dp[i - 1])

    if day <= n:
        dp[day] = max(dp[day], p+dp[i-1])

print(dp[-1])


