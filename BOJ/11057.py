# 1차원으로 만들기
# 애초에 dp를 덮어씌우는 느낌으로다가
N = int(input())

dp = [1] * 10

for i in range(N-1):
    for j in range(10):
        dp[j] = sum(dp[j:])

ans = sum(dp)
print(ans%10007)


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# dp = [[0]*10 for _ in range(n+1)]
#
# for i in range(10):
#     dp[0][i] = 1
#
# for i in range(1, n+1):
#     for j in range(10):
#         dp[i][j] = sum(dp[i-1][j:10])
#
# print(dp[n][0]%10007)


