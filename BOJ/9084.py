import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    coin = [0] + list(map(int, input().split()))
    money = int(input())

    dp = [[0] * (money+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        co = coin[i]
        # 0원이 되는경우도 항상 존재 -> 1
        dp[i][0] = 1

        for j in range(0, money+1):
            #
            dp[i][j] = dp[i-1][j]
            if j >= co:
                dp[i][j] += dp[i][j-co]

    # for i in dp:
    #     print(i)
    # print()
    print(dp[N][money])
