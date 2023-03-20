import sys

input = sys.stdin.readline

def NM(depth, i, idx):
    if depth == M:
        print(i.lstrip())
        return

    for j in range(idx, N):
        NM(depth+1, i + ' ' + str(data[j]), j)


N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

NM(0, '', 0)