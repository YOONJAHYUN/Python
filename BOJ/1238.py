import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
    visited = [1e9] * (N+1)
    visited[start[1]] = 0

    heap = []
    heappush(heap, start)

    while heap:
        time, now = heappop(heap)

        if visited[now] < time:
            continue

        for new_time, next in graph[now]:

            res = new_time + time

            if res < visited[next]:
                visited[next] = res
                heappush(heap, (res, next))

    return visited

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int,input().split())
    graph[start].append((time, end))

result = 0
lst = dijkstra((0, X))
# 가는데 걸리는 시간
for i in range(1, N+1):
    ans = dijkstra((0, i))[X]+lst[i]
    result = max(result, ans)

print(result)
# 오는데 걸리는시간
# print(dijkstra((0, X)))
'''
학생 1부터 N까지 중에서 가장 오래 걸리는 시간
'''