import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
node = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

q = []
visited = [False for _ in range(N+1)]

q.append(1)
visited[1] = True
#
# def f(n):
#
#     while q:
#
#         dot = q.popleft()
#
#         for i in node[dot]:
#             if visited[i] == 0:
#                 visited[i] = n
#                 q.append(i)
#
#     for i in range(1, N+1):
#         if visited[i] == 0:
#             q.append(i)
#             f(n+1)
#
# if M == 0:
#     print(N)
# else:
#     f(1)
#     print(max(visited))

#######################################
# 재귀를 쓰지말아봐요..#
if M == 0:
    print(N)
else:
    n = 1
    idx = 1
    while True:
        while q:

            dot = q.pop()

            for i in node[dot]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)

        for i in range(idx, N+1):
            if visited[i] == False and node[i]:
                q.append(i)
                idx = i
                n += 1
                break
        else:
            break
    print(n + visited.count(False) - 1)
####################################
# 시간 초과 개 짱 난 다
