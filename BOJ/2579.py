# 계단 오르기
import sys
input = sys.stdin.readline

N = int(input())
# 첫번째 계단은 계단이라 치지 않아서 일단 0을 넣어봤다..
scores = [0]

# 계단 점수 입력
for _ in range(N):
    scores.append(int(input()))

# 조건
# 1. i는 +1 or +2 가능
# 2. i, i+1, i+2 불가능
# 3. -1은 무조건

# N = 1이면 1 ->1개
# N = 2이면 (1 2) ->1개
# N = 3이면 (1 3) // (2 3) -> 2개

# N = 4이면 (1 3 4) // (1 2 4) -> 2개 // N =3 or N=2

# N = 5이면 (1 2 4 5) // (2 3 5) // (1 3 5) // (1 2 4 5) -> 3개 // N =4 or N=3

# N = 6이면 (1 2 4 6) // (2 3 5 6) // (1 3 4 6) // (1 3 5 6) -> 4개 // N =4 or N=5

# N = 7이면 (1 2 4 5 7) // (1 3 4 6 7) // (1 2 4 6 7) // (1 3 5 7) // (2 3 5 7) -> 5개 // N =5 or N=6

# N = 8이면 (1 2 4 5 7 8) // (2 3 5 6 8) // (1 3 5 7 8) //*(1 3 4 7 8)*// (2 3 5 7 8) -> 5개 // N =7 or N=6


dp = [0]*(N+1)
dp[1] = scores[1]
if N == 1:
    print(scores[1])
else:
    dp[2] = scores[1] + scores[2]

    for i in range(3, N+1):
        dp[i] = max((dp[i-3]+scores[i-1]), dp[i-2]) + scores[i]

    print(dp[N])