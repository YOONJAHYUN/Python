import sys
input = sys.stdin.readline

tc = int(input())
INF = int(1e9)

def bellman_ford(start):


    distance = [INF] * (n+1)
    distance[start] = 0

    for i in range(n):
        for edge in edges:
            current = edge[0]
            next = edge[1]
            cost = edge[2]

            if distance[next] > distance[current] + cost:
                distance[next] = distance[current] + cost

                if i == n-1:
                    return True

    return False


for _ in range(tc):
    # 지점의 수 n, 도로의 개수 m, 웜홈을 개수 w
    # 도로는 방향이 없고, 웜홀은 방향이 있다.
    n, m, w = map(int, input().split())


    # 연결된 도로
    edges = []
    for _ in range(m):
        # s e 연결된 지접의 번호, t 이동하는데 걸리는 시간
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))



    # 웜홀
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))


    result = bellman_ford(1)

    if result:
        print("YES")
    else:
        print("NO")



