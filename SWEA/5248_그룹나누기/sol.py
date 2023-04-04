import sys

sys.stdin = open('input.txt')

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y

    if rank[x] == rank[y]:
        rank[x] += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = list(map(int, input().split()))

    parent = list(range(N+1))

    rank = [0] * (N+1)
    # print(parent)

    for i in range(M):
        x = data[2*i]
        y = data[2*i+1]
        union(x,y)

    result = set()

    for i in range(1, N+1):
        result.add(find_set(i))

    print(f'#{tc}', len(result))