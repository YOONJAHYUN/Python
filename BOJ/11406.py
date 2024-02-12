import sys
from collections import deque
input = sys.stdin.readline

def BFS(source, sink, visited):

    q = deque()
    q.append(source)

    while q:
        if visited[sink] != -1:
            break

        now = q.popleft()

        for next_node in graph[now]


def edmonds_karp(source, sink):

    visited = [-1] * (m+1)
    if not BFS(source, sink, visited):
        break



# n 사람, m 온라인 서점
n, m = map(int, input().split())
graph = [[] for _ in range(m+1)]
flow = [[0] * (n+1) for _ in range(m+1)]

people = list(map(int, input().split()))
books = list(map(int, input().split()))

capacity = [list(map(int, input().split())) for _ in range(m)]

