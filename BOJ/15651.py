import sys

input = sys.stdin.readline

def NM(depth, i, N):
    if M == depth:
        print(i.lstrip())
        return

    for j in range(1, N+1):
        NM(depth+1, i + ' ' + str(j), N)


N, M = map(int, input().split())

NM(0, '', N)