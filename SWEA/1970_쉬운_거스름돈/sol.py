import sys

sys.stdin = open('input.txt')

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    N = int(input())
    result = []
    for don in money:

        if N < don:
            result.append(0)
        else:
            result.append(N//don)
            N = N % don
    print(f'#{tc}')
    print(*result)
