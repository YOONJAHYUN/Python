import sys
sys.stdin = open('input.txt')

def gold():

    for i in range(n):
        my_max = numbers[i:n]
        if numbers[i] < my_max:
            for j in range(i, n):
                if my_max == numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]



T = int(input())
for tc in range(1, T+1):
    numbers, cnt = map(str, input().split())
    cnt = int(cnt)
    n = len(numbers)
    numbers = list(numbers)
    print(numbers)

