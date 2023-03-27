import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(str, input()))

    # sort가 안된다.. 스스로 구해보자

    for i in range(6):
        for j in range(i, 6):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    # numbers.sort()
    # print(numbers)

    # run과 triplet으로만 구성되기 위해선 데이터의 0~2/3~6 까지로 나뉘어짐
    triplet = 0
    my_run = 0
    for i in range(2):
        if int(numbers[i]) == int(numbers[i+1]):
            triplet += 1
        elif int(numbers[i]) +1 == int(numbers[i+1]):
            my_run += 1

    for i in range(3, 5):
        if int(numbers[i]) == int(numbers[i+1]):
            triplet += 1
        elif int(numbers[i]) +1 == int(numbers[i+1]):
            my_run += 1

    # print(triplet, run)
    if (triplet == 2 and my_run == 2) or triplet == 4 or my_run == 4:
        print(True)
    else:
        print(False)