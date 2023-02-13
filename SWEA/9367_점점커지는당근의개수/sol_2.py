import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    result = 0
    count = 0
    for i in range(1, N):

        if C[i] == C[i-1] + 1:
            count += 1
            if i == N - 1:
                result = max(count + 1, result)
                count = 0
        else:
            result = max(count+1, result)
            count = 0

    print(f'#{tc}', result)