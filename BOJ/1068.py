import sys
input = sys.stdin.readline

N = int(input())
# 해당노드의 부모값 저장
parent = list(map(int, input().split()))
# 해당 노드의 자식 저장
# 해당 리스트가 빈 리스트이면 리프 노드임
children = [[] for _ in range(N)]
D = int(input())

for i in range(N):

    if parent[i] == -1:
        continue
    else:
        children[parent[i]].append(i)
# print(parent)
# print(children)

stack = []
stack.append(D)

while stack:

    node = stack.pop()
    if children[node]:
        for num in children[node]:
            stack.append(num)
    children[node] = [-1]

# D의 부모노드에서도 D값 제거
if parent[D] != -1:
    mom = parent[D]
    idx = children[mom].index(D)
    children[mom].pop(idx)

# print(children)
cnt = 0
for lst in children:
    if not lst:
        cnt += 1

print(cnt)



