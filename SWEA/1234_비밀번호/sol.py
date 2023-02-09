import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, number = map(int, input().split())
    numbers = []

    number = str(number)
    numbers.extend(number)
    i = 1

    while i != len(numbers):

        if numbers[i-1] == numbers[i]:
            numbers.pop(i-1)
            numbers.pop(i - 1)
            i = 1
        else:
            i += 1


    print(''.join(numbers))