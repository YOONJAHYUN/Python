import sys

sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    for i in range(1, N+1):
        if i**3 == N:
            print(f'#{tc}', i)
            break
        elif i**3 > N:
            print(f'#{tc}', -1)
            break
