import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):

    q = []
    heappush(q, start)

    while q:

        time, now = heappop(q)

        if visited[now] < time:
            continue

        for next_time, next in data[now]:
            res = next_time + time

            if res < visited[next]:
                visited[next] = res
                heappush(q, (res, next))


'''
output -> 총 감염되는 컴퓨터 수, 마지막까지 걸리는 시간
연결되어 있으므로 최소로 구해야함 -> 다익스트라
'''


t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())

    data = [[] for _ in range(n+1)]
    # a가 b를 의존하며 s초 후 컴퓨터 a도 감염됨
    for _ in range(d):
        a, b, s = map(int, input().split())
        data[b].append((s, a))

    visited = [int(1e9)] * (n+1)
    visited[c] = 0
    dijkstra((0, c))
    # print(visited)
    cnt = 0
    max_time = 0
    for i in visited:
        if i != int(1e9):
            cnt += 1
            max_time = max(max_time, i)

    print(cnt, max_time)
