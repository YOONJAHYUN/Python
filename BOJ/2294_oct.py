import sys
input = sys.stdin.readline

# 문어박사님 1차원 dp코드

n, k = map(int, input().split())
sset = set()

for _ in range(n):
    sset.add(int(input()))

# dp테이블 생성 및 초기화
INF = k+1
dp = [INF] * (k+1)

dp[0] = 0
# 원래 배열에 계속 덮어씌우는 방식
for coin in sset:
    for j in range(1, k+1):
        if j-coin >= 0:
            dp[j] = min(dp[j], dp[j-coin]+1)
ans = dp[k]

if ans == INF:
    ans = -1
print(ans)