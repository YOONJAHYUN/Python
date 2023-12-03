import sys
input = sys.stdin.readline


n = int(input())
data = list(map(int, input().split()))

dp = [1 for i in range(n)]
for i in range(n):
    dp[i] =data[i]
    for j in range(i):
        if (data[i] > data[j]) and (dp[i] < dp[j] + data[i]):
            dp[i] = dp[j] + data[i]
print(max(dp))