import sys

input = sys.stdin.readline

def NM(depth, lst):
    if depth == M:
        ans.append(lst)
        return

    prev = 0

    for j in range(N):
        if not visited[j] and prev != numbers[j]:
            prev = numbers[j]
            visited[j] = True
            NM(depth+1, lst+[numbers[j]])
            visited[j] = False

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
numbers.sort()
ans = []
visited = [False] * N
NM(0, [])

for i in ans:
    print(*i)