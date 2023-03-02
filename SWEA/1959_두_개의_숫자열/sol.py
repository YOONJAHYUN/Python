import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    total = 0
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 항상 N을 크게해서 M을 돌린다
    if N < M:
        N, M = M, N
        A, B = B, A
    # print(N, A)
    # print(M, B)
    for i in range(0, N-M+1):
        my_sum = 0
        for j in range(M):

            my_sum += (A[j+i] * B[j])
            # print(A[j])
        total = max(my_sum, total)
    print(f'#{tc}', total)