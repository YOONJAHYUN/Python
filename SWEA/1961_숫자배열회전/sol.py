import sys

sys.stdin = open('input.txt')

T = int(input())
##########################################################
for tc in range(T):
    N = int(input())

    arr1 = [[0] * N for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    arr3 = [[0] * N for _ in range(N)]


    numbers = []

    for i in range(N):
        numbers.append(list(map(int, input().split())))

    # print(numbers)
#############################################################
    for i in range(N):
        for j in range(N):
            arr1[i][j] = numbers[N-1-j][i]

    # for i in range(N):
    #     print(*arr1[i])
    #
##############################################################
    for i in range(N):
        for j in range(N):
            arr2[N-1-i][N-1-j] = numbers[i][j]
    #
    # for i in range(N):
    #     print(*arr1[i], '', *arr2[i])
##############################################################
    for i in range(N):
        for j in range(N):
            arr3[N-1-i][j] = numbers[j][i]
    print(f'#{tc+1}')
    for i in range(N):

        print(''.join(list(map(str, arr1[i]))),''.join(list(map(str, arr2[i]))),''.join(list(map(str, arr3[i]))))