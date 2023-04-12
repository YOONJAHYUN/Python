import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):

    heap = []
    v = [1e9] * (N + 1)

    # 내가 지나온 부분은 표시
    v[start[1]] = 0
    heappush(heap, start)

    while heap:

        cost, now = heappop(heap)
        if cost > v[now]:
            continue

        for new_cost, next in graph[now]:
            res = cost + new_cost

            if res < v[next]:

                v[next] = res
                heappush(heap, (res, next))

    return v


N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

'''
v1과 v2는 무조건 지나야한다.
그러기 위해서는 ?
이동한 경로를 표시해야함.
재귀가 아니라서 불가능..할듯..

그럼 1에서 v1까지, v1에서 v2까지, v2에서 N까지와
1에서 v2, v2-> v1, v1-> N까지구함

'''
route1 = dijkstra((0,1))[v1]+dijkstra((0,v1))[v2]+dijkstra((0,v2))[N]
route2 = dijkstra((0,1))[v2]+dijkstra((0,v2))[v1]+dijkstra((0,v1))[N]

# 같아도 안된다잉...
if route1 >= 1e9 and route2 >= 1e9:
    print(-1)
else:
    print(min(route1, route2))


