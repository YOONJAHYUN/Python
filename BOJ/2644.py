import sys
input = sys.stdin.readline

def DFS():
    global ans

    while stack:

        person, cnt = stack.pop(0)

        for i in people[person]:

            if i == num2:
                ans = cnt
                return

            if visited[i] == False:
                stack.append((i, cnt + 1))
                visited[i] = True

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())

people = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    # 부모에다가 자식 표시
    people[x].append(y)
    # 자식에다가 부모 표시
    people[y].append(x)

visited = [False] * (n+1)
# print(people)

stack = []
stack.append((num1, 1))
ans = -1
DFS()
print(ans)
