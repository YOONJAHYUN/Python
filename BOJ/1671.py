import sys

input = sys.stdin.readline

def bitmatch(now):

    for shark in graph[now]:
        if not visited[shark] and selected[shark] != now:
            visited[shark] = True

            # 아직 아무도 선택 안했거나, 선택했다면 교환이 가능하면
            if selected[shark] == -1 or bitmatch(selected[shark]):
                selected[shark] = now
                if selected.count(now) >= 2:
                    return True

    return False


n = int(input())

sharks = [list(map(int, input().split())) for _ in range(n)]


graph = [[] for _ in range(n)]

# 상어들을 비교해서 먹을 짝지를 짓는다.

for i in range(n):
    for j in range(i+1, n):
        if sharks[i][0] >= sharks[j][0] and sharks[i][1] >= sharks[j][1] and sharks[i][2] >= sharks[j][2]:
            graph[i].append(j)

        if sharks[i][0] <= sharks[j][0] and sharks[i][1] <= sharks[j][1] and sharks[i][2] <= sharks[j][2]:
            graph[j].append(i)

selected = [-1] * (n)

for i in range(n):

    visited = [False] * n
    bitmatch(i)

print(selected)
print(selected.count(-1))
