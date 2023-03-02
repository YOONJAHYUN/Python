import sys

input = sys.stdin.readline
# 논리에 오류가 있었다..
# 애초에 주사위 하나가 놓여지면 걔의 최댓값은 이미 정해져있다..
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

# for i in dice:
#     print(i)
# print()
total = 0
for q in range(6):
    # 주사위 눈 세기
    my_dice = [0] + [n for _ in range(6)]
    # 주사위 첫번째 넣기
    result = []
    result.append(dice[0][q])

    # 첫번째 값의 위 아래 눈금 빼주기
    my_dice[dice[0][q][0]] -= 1
    my_dice[dice[0][q][1]] -= 1
    print(my_dice)
    # 남은 주사위를 첫번째와 맞춰서 넣는다
    for i in range(1,n):

        for up, down in dice[i]:
            if result[-1][0] == down:
                result.append((up, down))
                # 주사위 눈만큼 빼줌
                my_dice[up] -= 1
                my_dice[down] -= 1
                # print(my_dice)
                break
    ans = 0
    cnt = 0
    print(q, result)
    print(q, my_dice)


    for i in range(6, 0, -1):
        # 남은 눈끼리 더해줌..
        while cnt < n:
            if my_dice[i] > 0:
                cnt += 1
                ans += i
                my_dice[i] -= 1
            else:
                break
    # print()
    # print(q, ans)
    # print()
    total = max(ans, total)
    print(q, ans)

print(total)

'''
6
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
2 3 1 6 5 4
'''

