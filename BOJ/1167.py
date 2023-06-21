import sys

input = sys.stdin.readline
INF = int(1e9)

def DFS(num, way):
    global ans

    distance = [INF] * (v+1)
    distance[num] = 0

    q = []
    q.append((0, num))

    while q:
        dist, now = q.pop()

        for next, dis in tree[now]:
            if distance[next] == INF:
                q.append((dist+dis, next))
                distance[next] = dist+dis

    my_max = 0
    idx = 0
    # distance에서 가장 먼 거리를 찾기
    for i in range(1, v+1):
        if my_max < distance[i]:
            my_max = distance[i]
            idx = i

    # print(distance)
    if way == 0:
        return idx
    else:
        return my_max

v = int(input())

tree = [[] for _ in range(v+1)]

for _ in range(v):
    data = list(map(int, input().split()))

    for i in range(1, len(data), 2):
        try:
            tree[data[0]].append((data[i], data[i+1]))
        except:
            break

# print(tree)
'''
1번부터 5번까지 dfs로 젤 먼데까지 걍 연결시키기 어떰?
-> 시간 초과
리프에서 리프가 그래도 젤 멀겠지? 리프만 구해보자
-> 이것도 시간 초과

아무 점(v)에서 시작해서 가장 먼 점(v1)을 찾고, 그 점(v1)에서 가장 먼 점(v2)를 찾으면,
v1과 v2 사이의 거리가 트리의 지름이됩니다. 다른 곳에도 응용되는 아이디어인 것 같더라구요.
'''
# print(gogo)
# 아무 점에서 시작해, 가장 먼 점을 찾기
start = DFS(1, 0)

print(DFS(start, 1))
