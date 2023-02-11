import sys

sys.stdin = open('input.txt')

def power(number, n):

    if n == 0:
        return 1
    else:
        return power(number, n-1) * number

for _ in range(1, 11):
    tc = int(input())
    number, n = map(int, input().split())
    print(f'#{tc}', power(number, n))

