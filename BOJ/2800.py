import sys

input = sys.stdin.readline

data = list(input().rstrip())
n = len(data)
open_gwal = []
close_gwal = []
idx = []
result = ''

# 괄호끼리 그룹을 만든다.
for i in range(n):
    if data[i] == '(':
        open_gwal.append(i)
    elif data[i] == ')':
        close_gwal.append(i)
    result += data[i]

print(open_gwal)
print(close_gwal)
print(idx)

# for i in range(len(open_gwal)):
#     for j in range(len(close_gwal)):
#
