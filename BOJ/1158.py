import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
people = deque(list(range(1, N+1)))

delete = []
while len(delete) != N:
    for _ in range(K-1):
        people.append(people.popleft())

    delete.append(people.popleft())
# print(delete)

# print('<', end='')
# for i in delete:
#     if i == delete[-1]:
#         print(i, end='')
#     else:
#         print(f'{i}, ', end='')
#
# print('>')

print('<', ', '.join(map(str,delete)), '>', sep='')

