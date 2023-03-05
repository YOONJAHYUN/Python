import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    idx_x = []

    for i in range(n):
        x = 0
        for j in range(n-1):

            if data[i][j] and data[i][j+1]:
                x += 1
            elif data[i][j] and not data[i][j+1]:
                x += 1
                idx_x.append(x)
                x = 0


    result = {}
    for i in range(len(idx_x)):
        result[idx_x[i]] = idx_x.count(idx_x[i])

    ans = sorted(result.items(), key=lambda x: (x[0]*x[1], x[1]))

    print(f'#{tc}', len(result), end=' ')

    for i, j in ans:
        print(j, i, end=' ')
    print()
