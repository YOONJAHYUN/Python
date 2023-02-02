import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    maximum = numbers[0]
    minimum = numbers[0]


    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    result = maximum - minimum

    print(f'#{i+1} {result}')