import sys
input = sys.stdin.readline

N = int(input())
data = [0] + list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    money = data[i]
    for j in range(1, N+1):
        if j-i >= 0:
            dp[i][j] = max(dp[i][j-i]+money, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])