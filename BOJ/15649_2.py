import sys

input = sys.stdin.readline

def NM(depth, N, i):

    if depth == M:

        print(i.lstrip())
        return

    for j in range(1, N+1):
        if not selection[j]:
            selection[j] = True
            NM(depth+1, N, str(i) + ' ' + str(j))
            selection[j] = False

N, M = map(int, input().split())

selection = [False] * (N+1)
NM(0, N, '')
