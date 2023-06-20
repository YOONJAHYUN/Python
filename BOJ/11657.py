import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

edges = []
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(start):

    # 시작 노드에서 초기화
    distance[start] = 0

    for i in range(n):
        # 모든 간선 확인
        for j in range(m):
            current = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[current] != INF and distance[next] > distance[current] + cost:
                distance[next] = distance[current] + cost
                # 마지막에도 값이 갱신된다면 음수 순환이 존재하는 것임
                if i == n-1:
                    return True

    return False

result = bellman_ford(1)
# 음수 순환이 존재하면 -1 출력
if result:
    print(-1)
else:
    # 최단 거리 출력
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])


