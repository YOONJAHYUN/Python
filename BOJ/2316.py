import sys
from collections import deque
input = sys.stdin.readline

n, p = map(int, input().split())
graph = [[] for _ in range(802)]
capacity = [[0] * 802 for _ in range(802)]
flow = [[0] * 802 for _ in range(802)]


for _ in range(p):
    s, e = map(int, input().split())

    s_in = s * 2 - 1
    s_out = s_in + 1

    e_in = e * 2 - 1
    e_out = e_in + 1

    # s ->e
    graph[s_out].append(e_in)
    graph[e_in].append(s_out)
    capacity[s_out][e_in] = 1

    # e -> s
    graph[e_out].append(s_in)
    graph[s_in].append(e_out)
    capacity[e_out][s_in] = 1

for i in range(1, n+1):
    s = i * 2 - 1
    e = s + 1
    graph[s].append(e)
    graph[e].append(s)
    capacity[s][e] = 1