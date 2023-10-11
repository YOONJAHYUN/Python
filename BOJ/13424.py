import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    visited = [INF for _ in range(n+1)]
    heappush(q, start)
    # 시작점 0
    visited[start[1]] = 0

    while q:

        distance, now = heappop(q)

        if visited[now] < distance:
            continue

        for next_distance, next in graph[now]:

            total = next_distance + distance

            if visited[next] > total:
                visited[next] = total

                heappush(q, (total, next))

    return visited

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    k = int(input())

    friends = list(map(int, input().split()))

    answer = [0 for _ in range(n+1)]

    for friend in friends:
        lst = dijkstra((0, friend))
        # print(lst)

        for num in range(1, n+1):
            answer[num] += lst[num]

    # print(answer)
    now = INF
    ans = 0
    for i in range(1, n+1):
        if answer[i] < now:
            now = answer[i]
            ans = i

    print(ans)
