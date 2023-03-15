import sys
input = sys.stdin.readline

def NM(depth, i):

    if depth == M:
        print(i.lstrip())
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            NM(depth+1, i + ' '+str(data[j]))
            visited[j] = False

N, M = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

# 백트래킹으로 풀어보자

visited = [False] * N
NM(0, '')
