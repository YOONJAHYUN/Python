import sys
input = sys.stdin.readline

t = int(input())
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(t):
    n = int(input())

    print(dp[n])
