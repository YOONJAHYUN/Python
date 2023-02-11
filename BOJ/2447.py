import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())

# 깊이를 활용해서 깊이에 맞는 크기를 만든다.
def star(n, depth, arr):
    # 전체 크기를 만든다.
    new_arr = [[0]*(3**depth) for _ in range(3**depth)]

    # 3**depth 가로크기로 지정해도됨. len(arr[i])
    for i in range(3**(depth-1)):
        for j in range(3**(depth-1)):
            for k in range(3):
                for l in range(3):
                    new_arr[i*3+k][j*3+l] = arr[i][j]

            new_arr[i*3+1][j*3+1] = ' '

    if 3 ** depth == n:
        return new_arr

    return star(n, depth + 1, deepcopy(new_arr))

base_arr = [["*"]]

answer = star(n, 1, base_arr)
for i in answer:
    print("".join(i))
