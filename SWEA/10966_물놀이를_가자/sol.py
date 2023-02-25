import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(input().rstrip()))

    water = []
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'W':
                water.append((i, j))

    result = 0
    for i in range(N):
        for j in range(M):
            location = []

            for wi, wj in water:
                location.append(abs(wi-i) + abs(wj-j))

            if location:
                result += min(location)

    print(f'#{tc}', result)
