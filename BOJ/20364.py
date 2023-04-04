import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
data = [0] * (N+1)


# duck = [int(input()) for _ in range(Q)]
# print(data)
# print(duck)

for i in range(1, Q+1):
    duck = int(input())

    moving_duck = duck
    # 계속 0으로 나누다가
    who = [0]
    # 내가 찜해둔자리가 중복될수도있음
    while moving_duck > 0:
        if data[moving_duck]:
            who.append(moving_duck)
        moving_duck //= 2
        # 그 자리에 누군가가있으면 못가는 거

            # print(moving_duck)
            # break
    # 지나갈 수 있었으면 데이터에 값 표기
    else:
        data[duck] = i
    print(who[-1])

