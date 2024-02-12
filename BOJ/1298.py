import sys

input = sys.stdin.readline

def bitmatch(now):

    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            if selected[i] == -1 or bitmatch(selected[i]):
                selected[i] = now
                return True
    return False


# n 사람 m 노트북 개수
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 노트북 -> 사람 선택
selected = [-1] * (n+1)

for i in range(1, n+1):
    visited = [False] * (n+1)
    bitmatch(i)

print(len(selected) - selected.count(-1))
