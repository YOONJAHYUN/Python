import sys

input = sys.stdin.readline

n, t = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    time, score = data[i-1]
    for j in range(1, t+1):
        if j - time >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + score)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])