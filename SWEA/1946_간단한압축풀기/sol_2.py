import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    alpha = ''
    for n in range(N):
        char, num = input().split()
        num = int(num)

        alpha += char * num

    print(f'#{tc}')

    for i in range(0, len(alpha), 10):
        print(alpha[0 + i:10 + i])