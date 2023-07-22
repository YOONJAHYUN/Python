import sys
from collections import deque
input = sys.stdin.readline

def path(x):
    answer = []
    answer.append(x)

    while x != n:
        x = move[x]
        answer.append(x)

    print(*answer[::-1])

def BFS(now):

    q = deque()
    q.append(now)

    while q:

        x = q.popleft()

        if x == k:
            print(visited[x])
            path(x)
            return x

        for i in (x+1, x-1, x*2):
            if 0 <= i <= 100000 and not visited[i]:
                q.append(i)

                visited[i] = visited[x] + 1
                # x에서 왔다 표시
                move[i] = x

n, k = map(int, input().split())

visited = [0] * 100001
move = [0] * 100001

BFS(n)
