import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def Binary(num, start, end, arr):

    if arr[start] > num:
        print(0)
        return

    if arr[end] < num:
        print(0)
        return

    if start == end:
        if num == arr[start]:
            print(1)
        return

    mid = (start + end) // 2

    if num == arr[mid]:
        print(1)
        return

    elif arr[mid] < num:
        return Binary(num, mid+1, end, arr)

    else:
        return Binary(num, start, mid-1, arr)

N = int(input())
list_N = list(map(int, input().split()))

list_N.sort()

M = int(input())
list_M = list(map(int, input().split()))

# 정수 범위가 2**-31에서 2**31임...
# 시간이 초과되니까 이진 탐색으로 해야한다...
# 이진 탐색 다 까먹었는데 어떡한담..

for num in list_M:
    Binary(num, 0, N-1, list_N)
# 아니 근데 이진탐색을 썼는데도 .. 시간초과가 나요;;;;
