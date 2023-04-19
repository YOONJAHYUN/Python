import sys
input = sys.stdin.readline

# 도시
n = int(input())
# 버스의 개수
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
road = [[[0] for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

# 버스의정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
    # 마지막노드를 미리정함
    road[a][b] = [a, b]

# 최소비용
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                # 마지막노드가있으니 갈 수있었으니까 그친구를 넣음
                road[j][k] = [*road[j][i], i, *road[i][k]]

# 최소비용
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        temp =[]
        for ans in road[i][j]:
            if ans not in temp:
                temp.append(ans)

        if len(temp) == 1:
            print(0)
        else:
            print(len(temp), *temp)