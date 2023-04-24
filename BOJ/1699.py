import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
dp = [0] *(n+1)

for i in range(1, n+1):
    if sqrt(i) == int(sqrt(i)):
        dp[i] = 1
    else:
        num = int(sqrt(i))**2
        while True:
            dp[i] += dp[num]

            if int(sqrt(i-num)**2) >= 1:
                dp[i] += dp[i-num]
                break
            num = int(sqrt(i-num)) **2

print(dp)