import sys

input = sys.stdin.readline

words = [list(input().rstrip()) for _ in range(2)]

n1 = len(words[0])
n2 = len(words[1])

arr = [[0]*(n1+1) for _ in range(n2+1)]
word = ''

for i in range(1, n2+1):
    for j in range(1, n1+1):
        if words[1][i-1] == words[0][j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[-1][-1])

# for i in arr:
#     print(i)

# 문자열 찾기
x, y = n1, n2

while x > 0 and y > 0:

    if arr[y][x] == arr[y][x-1]:
        x -= 1
    elif arr[y][x] == arr[y-1][x]:
        y -= 1
    else:
        word += words[0][x-1]
        x -= 1
        y -= 1

print(word[::-1])