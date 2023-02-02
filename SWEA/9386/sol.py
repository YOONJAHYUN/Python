import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    num = int(input())
    numbers = list(map(int, input()))

    count = 0
    max_count = 0

    for n in numbers:
        if n == 1:
            count += 1
            if count >= max_count:
                max_count = count
        else:
            count = 0
    print(f'#{tc+1}', max_count)




