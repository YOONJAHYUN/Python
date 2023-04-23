import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = data[0]
# 선택을 하고 안하고에 따라 답이 달라짐.
for i in range(1, n):
    # 나를 선택했을 때 뒤에꺼를 들고 올건지 말건지 선택.
    if data[i] + dp[i-1] > data[i]:
        dp[i] = data[i] + dp[i-1]
    else:
        dp[i] = data[i]

print(max(dp))