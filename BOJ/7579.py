import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
C = list(map(int, input().split()))
cost_sum = sum(C)

dp = [[0]*(cost_sum+1) for _ in range(n+1)]
answer = cost_sum+1

for i in range(1, n+1):
    memory = A[i-1]
    cost = C[i-1]
    for j in range(cost_sum+1):
        if j - cost < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost] + memory, dp[i-1][j])

        if dp[i][j] >= m:
            answer = min(j, answer)

print(answer)

