import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(n)]
# my_list = [int(1e9) for _ in range(n+1)]
# my_list[1]=A[0]
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            # if dp[i] < dp[j]+1:
                # dp[i] = dp[j]+1
                # my_list[dp[j]+1] = min(A[i], my_list[dp[j]+1])

            dp[i] = max(dp[i], dp[j]+1)
ans = max(dp)
print(ans)
# print(*my_list[1:ans+1])
result = []
idx = ans
for i in range(n-1, -1, -1):
    if dp[i] == idx:
        result.append(A[i])
        idx -= 1
print(*result[::-1])