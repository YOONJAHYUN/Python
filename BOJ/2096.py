import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(n):

    A, B, C = dp
    a, b, c = min_dp
    x, y, z = map(int, input().split())

    for j in range(3):

        if j == 0:
            dp[j] = max(A, B) + x
            min_dp[j] = min(a, b) + x

        elif j == 1:
            dp[j] = max(A, B, C) + y
            min_dp[j] = min(a, b, c) + y

        else:
            dp[j] = max(B, C) + z
            min_dp[j] = min(b, c) + z

print(max(dp), min(min_dp))

