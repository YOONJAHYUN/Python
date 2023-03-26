import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            home.append((i,j))
        elif data[i][j] == 2:
            chicken.append((i,j))

num_chi = len(chicken)
num_home = len(home)
# 살아있는 치킨집이 M과 같다면 그냥 치킨거리 다 더하기
if num_chi == M:
    D = 0
    for hi, hj in home:
        d = 13**6
        for ci, cj in chicken:
            d = min(abs(hi-ci) + abs(hj-cj), d)
        D += d
    print(D)

# 치킨집과 M이 다르다면, 살릴 치킨집을 선택한다.
# 치킨집과 home이 가까운게 몇개 있는지..?
else:
    D = [[] for _ in range(num_chi)]

    for i in range(num_chi):
        ci, cj = chicken[i]

        for hi, hj in home:
            d = abs(hi - ci) + abs(hj - cj)
            D[i].append(d)

        D[i].append(sum(D[i]))
    # M이 하나라면 그냥 거리가 젤 짧은 거 고른다.
    if M == 1:
        ans = 13**6
        for lst in D:
            ans = min(ans, lst[-1])
        print(ans)
    # M을 선택해야하는 경우
    # M 선택기준 : 거리가 젤 짧은 것을 고르고 그게 많은 것을 골라야됨
    else:
        combi = list(combinations(D, M))
        my_sum = 13 ** 6
        for i in D:
            print(i)
        for two in combi:
            C = [N ** 2] * num_home
            for lst in two:
                for idx in range(num_home):
                    C[idx] = min(C[idx], lst[idx])

            my_sum = min(my_sum, sum(C))
        print(my_sum)

        # 밑의 조건이 확실하게 맞다고 할 수 없음.. 오답
        # D.sort(key=lambda x: x[-1])

        # for i in D:
        #     print(i)
        # print()
        # C = [N**2] * num_home
        # for lst in D[0:M]:
        #     # print(lst)
        #     for idx in range(num_home):
        #
        #         C[idx] = min(C[idx], lst[idx])

        # print(sum(C))



