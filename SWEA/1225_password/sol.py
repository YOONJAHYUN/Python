import sys
from collections import deque
sys.stdin = open('input.txt')

for _ in range(1,11):
    tc = int(input())
    data = list(map(int, input().split()))

    # 5사이클 돌리면 다 똑같이 15씩 빠진다.
    # 5사이클을 몇 번씩 돌려야 하는지 계산하자.
    # 가장 큰 값을 기준으로 나머지를 구한다.
    my_max = max(data)
    cycle = int(my_max / 15) - 1

    # cycle만큼 모든 값을 빼준다.
    for i in range(8):
        data[i] -= cycle * 15
    # print(data)

    my_deque = deque(data)
    n = 1
    while True:

        first = my_deque.popleft()
        if first - n <= 0:
            my_deque.append(0)
            break
        else:
            my_deque.append(first - n)
            n += 1
            if n == 6:
                n = 1

    print(f'#{tc}', *my_deque)