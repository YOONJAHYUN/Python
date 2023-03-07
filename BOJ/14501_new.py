import sys
input = sys.stdin.readline

def consult():
    # 뒤에서 부터 체크한다.
    for day in range(N-1, -1, -1):
        # 며칠간의 상담인지 체크한다.
        t = data[day][0]

        # 해당 일에 근무하는 경우
        if day + t <= N:
            # 그때의 돈을 저장한다
            p = data[day][1]

            # 근무를 하는 경우와 하지 않는 경우 중 큰 값을 구한다.
            dp[day] = max(dp[day+1], dp[day+t]+p)

        # 해당 일에 근무하지 않는 경우
        else:
            dp[day] = dp[day+1]
        # print(day, dp)


N = int(input())

result = 0
data = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
consult()
print(dp[0])
