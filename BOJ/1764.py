import sys

input = sys.stdin.readline

N, M = map(int, input().split())

d_people = set(input().rstrip() for _ in range(N))
b_people = set(input().rstrip() for _ in range(M))

db = list(d_people & b_people)
db.sort()
print(len(db))
for person in db:
    print(person)