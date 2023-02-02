import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))


    # for문을 돌려서 각 숫자들의 합을 구해본다.
    num = []


    for j in range(N - M + 1):

        num_list = 0
        for k in range(M):
            num_list += numbers[j + k]


        num.append(num_list)



    sum_min = num[0]
    sum_max = num[0]

    for n in num:
        if n > sum_max:
            sum_max = n

        if n < sum_min:
            sum_min = n


    print(f'#{i+1}', sum_max-sum_min)




