# 내가 한거
# 2차원이라서 시간이 오래걸린다
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# h = int(n ** 0.5)
#
# dp = [[0 for _ in range(n+1)]]+[[i for i in range(n+1)]]+[[0] *(n+1) for _ in range(h)]
# # print(dp)
# for i in range(2, h+2):
#
#     for j in range(0, n+1):
#         if j >= i*i:
#             dp[i][j] = min(dp[i-1][j], dp[i][j-i*i]+1)
#         else:
#             dp[i][j] = dp[i-1][j]
# print(dp[-1][-1])

# 문박사님 코드
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# m = int(n**0.5)
#
# dp = [i for i in range(n+1)]
#
# for i in range(2, m+1):
#     for j in range(1, n+1):
#         if j > i*i:
#             dp[j] = min(dp[j], dp[j-i*i]+1)
# print(dp[n])

# 업그레이드 문박사
# 시간이 조금 더 준다
import sys
input = sys.stdin.readline

n = int(input())
m = int(n**0.5)

dp = [i for i in range(n+1)]

for i in range(2, m+1):
    for j in range(i*i, n+1):
        dp[j] = min(dp[j], dp[j-i*i]+1)
print(dp[n])