import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            continue
        # 왼쪽에 있는 경우 (가로)
        if j-1 >= 0:
            if dp[i][j-1][0]:
                dp[i][j][0] += dp[i][j-1][0]
            if dp[i][j-1][2]:
                dp[i][j][0] += dp[i][j-1][2]

        # 바로위
        if i - 1 >= 0:
            if dp[i-1][j][1]:
                dp[i][j][1] += dp[i-1][j][1]
            if dp[i-1][j][2]:
                dp[i][j][1] += dp[i-1][j][2]

        # 대각선
        if i - 1 >= 0 and j - 1 >= 0:
            if dp[i-1][j-1][0] and arr[i-1][j] != 1 and arr[i][j-1] != 1:
                dp[i][j][2] += dp[i-1][j-1][0]
            if dp[i-1][j-1][1] and arr[i-1][j] != 1 and arr[i][j-1] != 1:
                dp[i][j][2] += dp[i-1][j-1][1]
            if dp[i-1][j-1][2] and arr[i-1][j] != 1 and arr[i][j-1] != 1:
                dp[i][j][2] += dp[i-1][j-1][2]

# for i in dp:
#     print(i)

print(sum(dp[-1][-1]))