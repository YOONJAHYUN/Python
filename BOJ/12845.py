import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))

for i in range(n):
    ans = 0
    visited = [[False] for _ in range(n)]
    visited[i] = True

    idx = i

    if idx =