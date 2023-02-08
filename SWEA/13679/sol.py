import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

<<<<<<< HEAD
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):

=======
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    # idx = 0
    result = []

    for i in range(0, N - M + 1):  # 5-2+1 = 4
        for j in range(0, N - M + 1):

            my_sum = 0
            for l in range(M):
                for k in range(M):
                    my_sum += arr[i+l][j+k]
            result.append(my_sum)


    print(f'#{tc+1}',max(result))
>>>>>>> 4ffb2a77f758734987c9f462acbaa155f51f3e00
