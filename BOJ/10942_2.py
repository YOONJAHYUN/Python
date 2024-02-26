import sys
input = sys.stdin.readline


n = int(input())
data = [-1]+list(map(int, input().split()))
m = int(input())

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            break

        if i == j:
            dp[i][j] = 1
        else:
            if data[i] == data[j]:
                if i-1 < j + 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j+1]


for _ in range(m):
    a, b = map(int, input().split())
    print(dp[b][a])


