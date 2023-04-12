import sys

input = sys.stdin.readline

n = int(input())
arr = [[]*10 for _ in range(1001)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = 10

    elif i == 2:
        # 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
        dp[i] = 55

    elif i == 3:
        # 55 + 45 + 36 +28 +21 + 15 + 10 +6 +3 + 1
        dp[i] = 220

    else:
        # 220 + 210 +