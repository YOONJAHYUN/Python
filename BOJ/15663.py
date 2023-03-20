import sys

input = sys.stdin.readline

def NM(depth, i, ans):

    if depth == M:
        result = i.lstrip()
        if result not in ans[::-1]:
            ans.append(i.lstrip())
            print(result)
        return

    for j in range(0, N):
        if not selection[j]:
            selection[j] = True
            NM(depth+1, i + ' ' + str(numbers[j]), ans)
            selection[j] = False

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()
ans = []
selection= [False] * N
NM(0, '', [])