import sys
input = sys.stdin.readline




N = int(input())

result = 0
data = [list(map(int, input().split())) for _ in range(N)]

idx = 0
while idx <= N:
    consult = [0] * (N + 1)

    money_zip = 0
    for i in range(idx, N):
        days, money = data[i]
        # print(days, money)
        if not consult[i+1]:
            for day in range(i+1, i+days+1):

                if 0 < i+1 <= N+1 and 0 < i+days+1 <= N+1:
                    consult[day] = i+1

    for i in range(1, N+1):
        if i in set(consult):
            money_zip += data[i-1][1]
    result = max(result, money_zip)

    idx += 1


print(consult)
print(result)