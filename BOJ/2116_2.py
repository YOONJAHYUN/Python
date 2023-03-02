import sys

input = sys.stdin.readline

# 주사위의 개수
n = int(input())

dice = [[] for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    # 윗면, 밑면 집어넣기
    dice[i].append((data[0], data[5]))
    dice[i].append((data[1], data[3]))
    dice[i].append((data[2], data[4]))
    dice[i].append((data[3], data[1]))
    dice[i].append((data[4], data[2]))
    dice[i].append((data[5], data[0]))

total = 0
for q in range(6):
    # 주사위 첫번째 넣기
    result = []
    result.append(dice[0][q])

    # 남은 주사위를 첫번째와 맞춰서 넣는다
    for i in range(1,n):

        for up, down in dice[i]:
            if result[-1][0] == down:
                result.append((up, down))
                break
    ans = 0
    # print(q, result)

    for i in result:
        if 6 not in i:
            ans += 6
        elif 5 not in i:
            ans += 5
        elif 4 not in i:
            ans += 4

    total = max(ans, total)
    # print(q, ans)
print(total)
