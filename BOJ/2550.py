import sys

input = sys.stdin.readline

n = int(input())

switch = list(map(int, input().split()))

light = list(map(int, input().split()))

n1, n2 = len(switch), len(light)

dp = [[0] * (n1+1) for _ in range(n2+1)]

for i in range(1, n2+1):
    for j in range(1, n1+1):
        if switch[i-1] == light[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


# 스위치 번호 찾기
x, y = n1, n2
answer = []
while x > 0 and y > 0:

    if dp[y][x] == dp[y][x-1]:
        x -= 1
    elif dp[y][x] == dp[y-1][x]:
        y -= 1
    else:
        answer.append(switch[x])
        x -= 1
        y -= 1
answer.sort()
print(*answer)