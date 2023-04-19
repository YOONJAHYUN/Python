import sys
input = sys.stdin.readline

# 도시
n = int(input())
# 버스의 개수
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
road = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

# 버스의정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
    # 마지막노드를 미리정함
    road[a][b] = a

# 최소비용
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                # 마지막노드가있으니 갈 수있었으니까 그친구를 넣음
                road[j][k] = road[i][k]
            else:
                continue
            # graph[j][k] = min(graph[j][i]+ graph[i][k], graph[j][k])

# 최소비용
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

# i * n + j 번째 줄에는 도시 i에서 도시 j로 가는 최소비용에 포함되어 있는
# 도시의 개수 k
# 도시 i에서 도시 j로 가는 경로

# i와 j 표시



for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print(0)

        else:
            if road[i][j] == j:
                print(2, i, j)
            else:
                # 다 담아
                way = []
                # 도착지 담기
                way.append(j)

                # 맨마지막 방문한곳
                # q = []
                # q.append(road[i][j])
                end = j
                while end != i:
                    way.append(road[i][end])
                    end = road[i][end]
                # 출발지 담기
                # way.append(i)
                print(len(way), *way[::-1])
