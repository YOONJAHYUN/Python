import sys
input = sys.stdin.readline

# N 물품의 수, K 준서가 버틸 수 있는 무게
N, K = map(int, input().split())

my_bag = [(0,0)]

for _ in range(N):
    w, v = map(int, input().split())
    my_bag.append((w, v))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = my_bag[i]
    for j in range(1, K+1):
        # 무거워서 그 칸에 못담는다.
        if j < weight:
            # 걍 원래 있던 그대로
            dp[i][j] = dp[i-1][j]
        else:
            # 가방에 넣을 수 있다.
            # 원래 그대가 나은지
            # 새로 담는게 나은지 -> 내 무게를 담을 수 있는 거니까 그 꽉 찬 상태를 데려와
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)


print(dp[N][K])
