import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*(n+1) for _ in range(k)]
for i in range(n+1):
    dp[0][i] = 1

for i in range(1, k):

    for j in range(n+1):
        for m in range(j+1):
            dp[i][j] += dp[i-1][m]

# for i in dp:
#     print(i)
# 첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.
print(dp[-1][-1]%1000000000)