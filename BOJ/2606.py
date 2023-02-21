import sys
input = sys.stdin.readline

# 컴퓨터 수
N = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터의 쌍의 수
C = int(input())

node = [[] for _ in range(N+1)]
for _ in range(C):
    v1, v2 = map(int, input().split())
    node[v1].append(v2)
    node[v2].append(v1)

# print(node)

stack = []
visited = [False for _ in range(N+1)]
stack.append(1)
visited[1] = True

count = -1
while stack:

    computer = stack.pop()
    count += 1
    for i in node[computer]:
        if visited[i] == False:
            stack.append(i)
            visited[i] = True

print(count)