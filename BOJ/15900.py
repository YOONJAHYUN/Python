import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# 리프에서 루트까지 갈 때까지 숫자를 세고 짝수 or 홀수 판단
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
q = []
q.append((1, 0))
visited[1] = True
baby = [0] * (N+1)
count = [0] * (N+1)
while q:
    num, cnt = q.pop()

    for number in tree[num]:
        if not visited[number]:
            q.append((number, cnt+1))
            visited[number] = True
            count[number] = cnt + 1

            if baby[num] == 0:
                baby[num] = 1
my_sum = 0
for i in range(1, N+1):
    if not baby[i]:
        my_sum += count[i]

# print(baby)
# print(my_sum)

if my_sum % 2:
    print('Yes')

else:
    print('No')





