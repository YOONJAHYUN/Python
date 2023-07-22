import sys
from collections import deque
input = sys.stdin.readline

# 사람수 n 파티수 m
n, m = map(int, input().split())

people = [[] for _ in range(n+1)]
# 진실을 아는 사람
tn, *true = map(int, input().split())


data = []
for _ in range(m):
    pn, *numbers = map(int, input().split())
    data.append((pn, numbers))
    for i in range(pn):
        for j in range(i, pn):
            person1 = numbers[i]
            person2 = numbers[j]

            if person1 not in people[person2]:
                people[person2].append(person1)

            if person2 not in people[person1]:
                people[person1].append(person2)


# print(people)
cnt = 0

for pn, numbers in data:

    q = deque()

    visited = [False] * (n+1)

    for number in numbers:
        q.append(number)
        visited[number] = True

    while q:

        now = q.popleft()

        if now in true:
            break

        for next in people[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

    else:
        cnt += 1

print(cnt)

'''         
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5

ans = 0
'''