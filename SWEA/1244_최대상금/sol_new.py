import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    numbers, cnt = map(int, input().split())
    numbers = list(map(int, list(str(numbers))))
    print(numbers)