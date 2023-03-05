import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = N
    numbers = []
    idx = 1
    lst = list(range(0, 10))
    while True:
        number = N * idx
        for i in str(number):
            if int(i) not in numbers:
                numbers.append(int(i))
        numbers.sort()
        if numbers == lst:
            break
        else:
            idx += 1

    print(f'#{tc}', number)