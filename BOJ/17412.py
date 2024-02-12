import sys
from collections import deque
input = sys.stdin.readline

def BFS(source, sink, visited):
    q = deque()
    q.append(source)

    while q:

        if visited[sink] != -1:
            return True

        now = q.popleft()

        for next_node in graph[now]:
            if capacity[now][next_node] - flow[now][next_node] > 0 and visited[next_node] == -1:
                visited[next_node] = now
                q.append(next_node)

                if next_node == sink:
                    break

    # 경로를 다 돌았는데 싱크를 못찾았을 경우
    return False

def edmonds_karp(source, sink):
    answer = 0

    while True:
        visited = [-1] * (n+1)
        # 경로를 못찾는 경우 중지
        if not BFS(source, sink, visited):
            break
        # 경로가 있다
        j = sink

        while j != source:
            i = visited[j]
            flow[i][j] += 1 # 지나갔음 의미
            flow[j][i] -= 1 # 음의 유량 추가
            j = i

        answer += 1
    return answer


n, p = map(int, input().split())

graph = [[] for _ in range(401)]
capacity = [[0]*401 for _ in range(401)]
flow = [[0]*401 for _ in range(401)]

for _ in range(p):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 음의 유량을 고려해서 양방향으로 추가함
    capacity[s][e] = 1 # 한 경로에 포함된 길이 다른 경로에 포함되면 안되므로 용량이 1임


print(edmonds_karp(1, 2))