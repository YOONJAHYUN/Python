import sys

input = sys.stdin.readline

def NM(depth, i, idx):

    if depth == M:
        print(i.lstrip())
        return
    prev= 0
    for j in range(idx, N):
        if prev != numbers[j]:
            prev = numbers[j]
            NM(depth + 1, i + ' ' + str(numbers[j]), j)

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

NM(0, '', 0)