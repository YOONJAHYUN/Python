import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    bus_stop = [0]*5001
    for n in range(N):
        a, b = map(int, input().split())

        for stop in range(a, b+1):
            bus_stop[stop] += 1

    P = int(input())
    c = []
    for _ in range(P):
        c.append(int(input()))

    stop_list = []
    for stop in c:
        stop_list.append(bus_stop[stop])

    print(f'#{tc}', *stop_list)