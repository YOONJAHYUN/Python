import sys

input = sys.stdin.readline

def NM(depth, i):
    if depth == M:
        print(i.lstrip())
        return

    for j in range(N):
        NM(depth+1, i + ' ' + str(data[j]))


N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

NM(0, '')