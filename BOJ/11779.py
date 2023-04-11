import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    # global result
    # global route
    q = []

    heappush(q, start)

    while q:
        cost, now = heappop(q)
        #
        # if v[now] < cost:
        #     continue
        #
        # for new_cost, new_location, new_route in graph[now]:
        #     res = new_cost + cost
        #     if res < v[new_location]:
        #         v[new_location] = res
        #         new_route.append(new_location)
        #         print(new_route)
        #         # route[new_location].append(now)
        #         heappush(q,(res, new_location, new_route))

        if visited[now][0] < cost:
            continue

        for new_cost, new_location in graph[now]:
            res = new_cost + cost

            if res < visited[new_location][0]:
                visited[new_location][0] = res
                visited[new_location][1] = now
                # for dir in visited[now][1]:
                #     visited[new_location][1].append(dir)

                heappush(q,(res, new_location))


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
# v = [int(1e9)] * (n+1)
# route = [[] for _ in range(n+1)]
visited = [[int(1e9), 0] for _ in range(n+1)]
# print(visited)
result = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

s, e = map(int, input().split())
visited[s][0] = 0

# v[s] = 0
dijkstra((0, s))
end = e
while end != s:
    result.append(end)
    end = visited[end][1]

# print(result)


# 최소비용
# print(visited)
print(visited[e][0])
print(len(result)+1)
print(s, *result[::-1])
'''
5
10
1 2 0
1 3 15
1 4 10
1 5 10
2 4 2
3 4 8
4 3 1
3 5 3
4 3 1
4 5 9
1 5
'''