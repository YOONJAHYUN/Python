import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    pizza = deque()
    pizza_hot = deque()
    for i in range(len(C)):
        pizza.append((i+1, C[i]))

    # print(pizza)

    # 기본 피자를 넣었음
    for _ in range(N):
        pizza_hot.append(pizza.popleft())
    # print(pizza_hot)


    # 피자를 구워보자
    while True:
        idx, one = map(int, pizza_hot.popleft())
        one = one // 2

        if one == 0:
            if pizza:
                pizza_hot.append(pizza.popleft())
            else:
                if len(pizza_hot) == 1:
                    print(f'#{tc}', pizza_hot[0][0])
                    break
                else:
                    continue
        else:
            pizza_hot.append((idx, one))

