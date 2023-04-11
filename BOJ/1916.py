import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
M = int(input())

# 1에서 출발 할 수 있는것, 2에서 출발...이런식으로 모으기
graph =[[] for _ in range(N+1)]
visited = [int(1e9)] * (N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

# for i in graph:
#     print(i)

s, e = map(int, input().split())

# (0, s) 현재까지의 cost 0, 시작점 s
def dijkstra(start):
    q = []
    # (0, s)
    heappush(q, start)

    while q:
        # (0, s)
        cost, now = heappop(q)

        # 최소값이 맞는지 확인
        # visited[now] 에 최댓값이 들어가있음
        if visited[now] < cost:
            continue
2
        # 아니라면? ->최소값으로 바꿔주기

        for i in graph[now]:
            # 지금가격에 거기방문시가격을 더해
            res = cost + i[0]
            # 만약에 그 가격이 더 저렴하면
            if res < visited[i[1]]:
                # 바꿔주고
                visited[i[1]] = res
                # heappush로 q에다가 (가격과, 노드번호)주기
                heappush(q, (res, i[1]))


dijkstra((0, s))
print(visited[e])