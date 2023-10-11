import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    if n == m:
        print(1)
    else:
        dp = [[0] * m for _ in range(n)]
        dp[0] = [i for i in range(1, m+1)]

        for i in range(1, n):
            for j in range(i, m):
                if j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

        print(dp[-1][-1])