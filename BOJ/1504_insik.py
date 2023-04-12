import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(go):
    global result1, result2
    visited = [int(1e9)] * (N + 1)
    visited[go[1]] = 0
    heap = []
    heappush(heap, go)
    while heap:
        cost, now = heappop(heap)
        if visited[now] < cost:
            continue
        for check in edge[now]:
            total = cost + check[0]
            if total < visited[check[1]]:
                visited[check[1]] = total
                heappush(heap, [total, check[1]])
    if go[1] == 1:
        result1 += visited[exam_node1]
        result2 += visited[exam_node2]
        return
    elif go[1] == exam_node1:
        result1 += visited[exam_node2]
        result2 += visited[N]
        return
    elif go[1] == exam_node2:
        result1 += visited[N]
        result2 += visited[exam_node1]
        return


N, E = map(int, input().split())

edge = [[] for _ in range(N + 1)]
for node in range(E):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])
    edge[end].append([distance, start])

exam_node1, exam_node2 = map(int, input().split())

result1 = 0
result2 = 0

dijkstra([0, 1])
dijkstra([0, exam_node1])
dijkstra([0, exam_node2])

if result1 >= int(1e9) and result2 >= int(1e9):
    print(-1)
else:
    if result1 >= result2:
        print(result2)
    else:
        print(result1)
'''
[1000000000, 0, 3, 5, 4]
[1000000000, 3, 0, 3, 4]
[1000000000, 5, 3, 0, 1]
7
'''