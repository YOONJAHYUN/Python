import sys
from heapq import heappop, heappush
input = sys.stdin.readline

'''
출발지 : 1
도착지 : V
중간 들리면 좋은 곳: P
'''
def dijkstra(start):
    global answer
    q =[]
    heappush(q, start)

    while q:

        distance, now, lst = heappop(q)

        if visited[now] < distance:
            continue

        if now == v:
            # print(lst, v)
            if p in lst:
                answer = "SAVE HIM"
            elif p not in lst and not answer:
                answer = "GOOD BYE"

        for next_distance, next in graph[now]:

            total = next_distance + distance

            if total <= visited[next]:
                visited[next] = total
                heappush(q, (total, next, lst+[now]))


v, e, p = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
visited = [INF for _ in range(v+1)]
answer = ""

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


dijkstra((0, 1, []))
# 최솟값 구함,
# print(visited)
print(answer)


