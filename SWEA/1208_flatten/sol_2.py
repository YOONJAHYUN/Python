import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    dump = list(map(int, input().split()))
    dump.sort()
    # print(dump)

    for _ in range(n):
        dump[0] += 1
        dump[99] -= 1
        dump.sort()

    print(dump[99]-dump[0])
