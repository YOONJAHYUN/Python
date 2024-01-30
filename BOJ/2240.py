import sys

input = sys.stdin.readline

t, w = map(int, input().split())
data = [int(input()) for _ in range(t)]

dp = [1] * t

print(dp)

for i in range(1, t):
    if data[i] == data[i-1]:
        dp[i] += dp[i-1]
    else:
        dp[i] = max(dp[i-1] + 1, )

print(dp)