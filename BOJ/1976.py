import sys
input = sys.stdin.readline

# 첫줄에 도시의 수
n = int(input())
# 여행 계획에 속한 도시의 수 m
m = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

plans = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if data[j][i] and data[i][k]:
                data[j][k] = 1

    data[i][i] = 1

# for i in data:
#     print(i)

for i in range(m-1):
    plan1 = plans[i] - 1
    plan2 = plans[i+1] - 1
    if not data[plan1][plan2]:
        print('NO')
        break
else:
    print('YES')

