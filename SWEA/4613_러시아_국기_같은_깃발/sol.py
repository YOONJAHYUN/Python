import sys
from itertools import *
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(input().rstrip()) for _ in range(N)]

    # for i in data:
    #     print(i)
    # print()
    cnt = 0
    # 첫줄은 무조건 W
    first = M -data[0].count('W')
    cnt += first
    # print(first)
    # 마지막 줄은 무조건 R
    last = M -data[-1].count('R')
    cnt += last

    lst = ['W', 'B', 'R']
    combi = list(combinations_with_replacement(lst, N-2))

    WBR = []
    for i in combi:
        if 'B' in i:
            WBR.append(i)
    # print(WBR)

    color_count = M*N
    for color in WBR:
        count = 0
        for i in range(N - 2):
            # print(color)
            # print(data[i+1])
            # print(color[i], data[i+1].count(color[i]))
            count += (M -data[i+1].count(color[i]))
        color_count = min(color_count, count)
    print(f'#{tc}', color_count+cnt)