import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())

    data = [[0]+list(map(int,input().split())) for _ in range(2)]
    # 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합
    dp = [[0]*(n+1) for _ in range(2)]

    dp[0][1] = data[0][1]
    dp[1][1] = data[1][1]

    for i in range(2, n+1):
        for j in range(2):
            dp[j][i] = max(dp[j][i-2], dp[j-1][i-1], dp[j-1][i-2]) + data[j][i]

    print(max(dp[0][-1], dp[1][-1]))