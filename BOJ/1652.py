# 누울자리를 찾아라
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(str, *input().split())) for _ in range(N)]

# print(arr)

# 연속한 '.'의 개수를 세고 2이상이면 +1
result1 = 0
for i in range(N):
    count = 0
    for j in range(N):
        if arr[i][j] == '.':
            count += 1
            if j == N-1 and count >= 2:
                result1 += 1
                count = 0
        else:
            if count >= 2:
                result1 += 1
                count = 0
            else:
                count = 0

result2 = 0
for i in range(N):
    count = 0
    for j in range(N):
        if arr[j][i] == '.':
            count += 1
            if j == N-1 and count >= 2:
                result2 += 1
                count = 0
        else:
            if count >= 2:
                result2 += 1
                count = 0
            else:
                count = 0

print(result1, result2)


