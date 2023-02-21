import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = list(map(int, input().split()))

    # my_deque = deque(data)
    #
    # for _ in range(M):
    #     my_deque.append(my_deque.popleft())

    print(f'#{tc}', data[M%N])