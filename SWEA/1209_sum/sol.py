import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    result1 = 0
    my_sum3 = 0
    my_sum4 = 0
    for i in range(100):
        my_sum1 = 0
        my_sum2 = 0
        for j in range(100):
            my_sum1 += arr[i][j]
            my_sum2 += arr[j][i]
        result1 = max(result1, my_sum1, my_sum2)
        my_sum3 += arr[i][i]
        my_sum4 += arr[i][99-i]

    print(f'#{tc}', max(result1, my_sum3, my_sum4))



