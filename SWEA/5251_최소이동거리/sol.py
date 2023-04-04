import sys

sys.stdin = open('input.txt')

def min_route(start, end, visit):
    global result
    if start == end:
        result = min(result, visit)
        # print(visit)
        return
    if visit > result:
        return
    if data[start][end] != 0:
        min_route(end, end, visit+data[start][end])

    for i in range(N):
        if data[start][i] != 0:
            min_route(i, end, visit+data[start][i])


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())

    data = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        data[s][e] = w

    # for i in data:
    #     print(i)
    # print()
    result = 1e9
    min_route(0, N, 0)

    print(f'#{tc}', result)
