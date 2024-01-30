import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]

max_answer = - n * m
min_answer = n*m
prefixSum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, 1+n):
    for j in range(1, 1+m):
        # 짝수인 경우
        if (i + j) % 2 == 0:
            if arr[i-1][j-1] == "B":
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
            else:
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + 1

        else:
            if arr[i-1][j-1] == "W":
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
            else:
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + 1

for i in range(1, n - k + 2):
    for j in range(1, m - k + 2):
        max_answer = max(max_answer, prefixSum[i + k - 1][j + k - 1] - prefixSum[i + k - 1][j - 1] - prefixSum[i - 1][j + k - 1] + prefixSum[i - 1][j - 1])
        min_answer = min(min_answer, prefixSum[i + k - 1][j + k - 1] - prefixSum[i + k - 1][j - 1] - prefixSum[i - 1][j + k - 1] + prefixSum[i - 1][j - 1])
print(min(min_answer, k*k - max_answer))
