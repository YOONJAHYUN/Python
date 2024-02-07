import sys
input = sys.stdin.readline

def bitmatch(work):

    nn = data[work][0]
    for i in range(1, nn+1):
        now = data[work][i]
        if not visited[now]:
            visited[now] = True
            if selected[now] == -1 or bitmatch(selected[now]):
                selected[now] = work
                return True

    return False

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
# 일을 체크
selected = [-1] * (m+1)

for i in range(n):
    visited = [False] * (m+1)
    bitmatch(i)
# print(selected)
print(len(set(selected))-1)


