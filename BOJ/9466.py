import sys
input = sys.stdin.readline

def DFS(now):

    q = []
    q.append(now)
    visited[now] = True
    check.append(now)

    while q:
        student = q.pop()

        if not visited[data[student]]:
            visited[data[student]] = True
            check.append(data[student])
            q.append(data[student])

        elif data[student] in check:
            result.extend(check[check.index(data[student]):])


'''
사이클이 만들어져야 한 팀이 될 수 있다.
어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산
'''

t = int(input())

for _ in range(t):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    result = []
    visited = [True] + [False] * (n)
    for i in range(1, n+1):
        if not visited[i]:
            check = []
            DFS(i)

    print(n - len(result))