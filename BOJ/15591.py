import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, q = map(int, input().split())
graph = defaultdict(list)

'''
유사도가 k1이상인 모든 동영상을 추천
graph[v1] 에서 유사도와 다음 정점을 뽑고, 거기서 유사도가 k1이상이면, q에 넣는다.

1번과 2번 -> 3
2번과 4번 -> 4
=>
1번과 4번 -> 3
'''
for _ in range(n-1):
    p, q, r = map(int, input().split())
    graph[p].append((r, q))
    graph[q].append((r, p))

for _ in range(q):
    k, v = map(int, input().split())
    visited = [False] * (n+1)
    visited[v] = True
    que = deque()
    que.append((int(1e9), v))
    cnt = 0

    while que:

        k1, v1 = que.popleft()

        for k2, v2 in graph[v1]:
            usado = min(k1, k2)

            if usado >= k and not visited[v2]:
                cnt += 1
                visited[v2] = True
                que.append((usado, v2))

    print(cnt)
