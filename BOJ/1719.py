import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

road = [[0]*(n+1) for _ in range(n+1)]



for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t

for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # 경로중에 더 최단경로가 있다면
            if graph[j][k] > (graph[j][i] + graph[i][k]):
                # 경로의 시간을 표기
                graph[j][k] = graph[j][i] + graph[i][k]

                # 제일 먼저뭐가갈지는
                road[j][k] = i
            else:
                continue


for i in range(1, n+1):
    for j in range(1, n+1):

        # 더빠른경로가있다
        if road[i][j]:
            # 그 경로의 마지막임
            mom = road[i][j]
            # 마지막의 엄마를 찾아야됨
            while True:
                #
                mom = road[mom][i]

                if mom:
                    road[i][j] = mom

                else:
                    break

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print('-', end=' ')

        elif road[i][j]:
            print(road[i][j], end=' ')
        else:
            print(j, end=' ')
    print()