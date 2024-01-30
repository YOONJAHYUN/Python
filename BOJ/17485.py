import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(3):
        dp[0][i][j] = arr[0][i]


for i in range(1, n):
    for j in range(m):
        for k in range(3):

            if (j == 0 and k == 2 ) or (j == m-1 and k == 0):
                dp[i][j][k] = int(1e9)
                continue

            if k == 0:
                dp[i][j][k] = min(dp[i-1][j+1][k+1], dp[i-1][j+1][k+2]) + arr[i][j]
            elif k == 1:
                dp[i][j][k] = min(dp[i-1][j][k+1], dp[i-1][j][k-1]) + arr[i][j]
            else:
                dp[i][j][k] = min(dp[i-1][j-1][k-2], dp[i-1][j-1][k-1]) + arr[i][j]
ans = int(1e9)
for i in dp[-1]:
    ans = min(min(i), ans)
print(ans)
