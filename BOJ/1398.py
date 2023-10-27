import sys
input = sys.stdin.readline

t = int(input())
dp = [int(1e9)] * (100)
dp[0] = 0
coins = [1, 10, 25]

for i in range(100):
    for coin in coins:
        if i + coin >= 100:
            continue
        dp[i+coin] = min(dp[i+coin], dp[i]+1)

for _ in range(t):
    cost = int(input())

    answer = 0
    while cost:
        answer += dp[cost % 100]
        cost //= 100
    print(answer)