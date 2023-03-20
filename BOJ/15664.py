import sys

input = sys.stdin.readline

def NM(depth, i, idx):
    if depth == M:
        print(i.lstrip())
        return
    prev = 0
    for j in range(idx, N):
        if not selection[j] and prev != numbers[j]:
            selection[j] = True
            prev = numbers[j]
            NM(depth+1, i + ' '+ str(numbers[j]), j+1)
            selection[j] = False
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
selection = [False] * N
numbers.sort()

NM(0, '', 0)