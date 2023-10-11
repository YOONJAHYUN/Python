import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def BFS(num):

    q = []
    heappush(q, (0, num))


    while q:

        count, now = heappop(q)

        if now == 100:
            print(count)
            return

        if data[now]:
            # if not visited[data[now]]:
            heappush(q, (count, data[now]))

                # q.append((data[now], count))
                # visited[now] = True

        else:

            for i in range(1, 7):
                next = now + i

                if next <= 100 and not visited[next]:
                    visited[next] = True
                    heappush(q, (count+1, next))

                    # q.append((next, count+1))


# n 사다리수 m 뱀의 수
n, m = map(int, input().split())

data = [0 for _ in range(101)]
visited = [False for _ in range(101)]
visited[1] = True

for _ in range(n):
    x, y = map(int, input().split())
    data[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    data[u] = v
# print(data)
BFS(1)





