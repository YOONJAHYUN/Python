import sys
input = sys.stdin.readline

n = int(input())
data = [0] + list(map(int, input().split()))

dp = [0] * (n+1)


# 나보다 큰 값중에서 젤 큰값 들고오기
for i in range(1, n+1):
    for j in range(0, i):
        if data[i] > data[j]:
            dp[i] = max(dp[j] + 1, dp[i])


print(max(dp))