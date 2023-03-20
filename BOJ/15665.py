import sys

input = sys.stdin.readline

def NM(depth, i):

    if depth == M:
        print(i.lstrip())
        return
    prev = 0
    for j in range(N):
        if prev != numbers[j]:
            prev = numbers[j]
            NM(depth+1, i + ' ' + str(numbers[j]))

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

NM(0, '')