import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    minV = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if C[i] != C[i+1] and C[j] != C[j+1]:
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A * B * C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    if minV > max(A, B, C) - min(A, B, C):
                        minV - max(A, B, C) - min(A, B, C)
1
    print(f'#{tc}', minV)
