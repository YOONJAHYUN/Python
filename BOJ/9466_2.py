import sys

input = sys.stdin.readline

'''
for문으로 하나씩 방문한다.
그리고 다음 걸 방문한다. 다음걸 방문하는데 사이클이 만들어지지 않으면
거기에 해당하는 모든 visited는 버린다.

'''

t = int(input())

for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):

        if not visited[i]:
            visited[i] = True
            q = [i]
            temp = []

            while q:
                student = q.pop()

                if student == students[student]:
                    result.append(student)
                    break

                if not visited[students[student]]:
                    visited[students[student]] = True
                    q.append(students[student])

                temp.append(student)

            if temp and students[temp[-1]] in temp:
                result.extend(temp[temp.index(students[temp[-1]]):])

    print(n - len(result))
