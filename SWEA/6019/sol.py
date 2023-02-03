import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    D, A, B, F = map(int, input().split())

    result = (D / (A + B)) * F

    a = float(result)
    print(f'#{tc+1}', f'{result:.10f}')