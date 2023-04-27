import sys
input = sys.stdin.readline

# 고객을 적어도 C명 늘려야됨
# 홍보할 수 있는 도시의 개수 N
C, N = map(int, input().split())
max_people = 0
data = []
for _ in range(N):
    cost, people = map(int, input().split())
    data.append((cost, people))
    max_people = max(max_people, people)
INF = int(1e9)
dp = [[INF]*(C+1+max_people) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = 0
# 호텔의 고객을 적어도 C명 늘이기 위해
for i in range(1, N+1):
    money = data[i-1][0]
    people = data[i-1][1]
    for j in range(1, C+1+max_people):
        if j >= people:
            dp[i][j] = min(dp[i-1][j], dp[i][j-people]+money)
        else:
            dp[i][j] = dp[i-1][j]
print(min(dp[-1][C:]))