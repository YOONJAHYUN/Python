import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

data = []

data.extend(map(int, input()))

answer = []
answer.extend(input().rstrip())

visited = {}

q = deque()

q.append((data, 0))

print(data)

# while q:
#
#     char_list, cnt = q.popleft()
#     char = ''.join(char_list)
#
#     if char == answer:
#         print(cnt)
#         break
#
#     for i in range(n):
#
#         if i != 0 and i != n-1:
#             char[i-1], char[i], char[i+1] = str(abs(1-int(char[i-1]))), str(abs(1-int(char[i]))), str(abs(1-int(char[i+1])))
#         elif i == 0:
#             char[i], char[i+1] = str(abs(1-int(char[i]))), str(abs(1-int(char[i+1])))
#         else:
#             char[i-1], char[i] = str(abs(1-int(char[i-1]))), str(abs(1-int(char[i])))
#
#         temp_char = ''.join(char)
#
#         if visited.get(temp_char):
#             continue
#         else:
#             visited[temp_char] = 1
#             q.append((temp, cnt+1))
