import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [0] * (n+1)
data = [0] * (n+1)

for _ in range(m):
    vip = int(input())
    data[vip] = 1
    # data[vip+1] = vip

# print(dp)
dp[1] = 1
if n >= 2:
    if(data[1] or data[2]):
        dp[2] = 1

    else:
        dp[2] = 2

    for i in range(3, n+1):

        if data[i] or data[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])