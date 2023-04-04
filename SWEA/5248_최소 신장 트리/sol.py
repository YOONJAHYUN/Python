import sys

sys.stdin = open('input.txt')

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, 1+T):
    V, E = map(int, input().split())

    tree = [list(map(int, input().split())) for _ in range(E)]

    # 가중치로 정렬
    tree.sort(key=lambda x:x[2])

    # 대표 원소 설정하기
    parent = list(range(V+1))

    ans = 0
    for v1, v2, w in tree:
        # 두개 노드의 부모가 다르면 (사이클이 아니란 소리)
        if find_set(v1) != find_set(v2):
            # 집합으로 만들어준다.
            union(v1, v2)
            ans += w
    print(f'#{tc}',ans)