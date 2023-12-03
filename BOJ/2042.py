import sys
from math import ceil, log
input = sys.stdin.readline

# 세그먼트 트리 구현
def segment(left, right, i=1):

    if left == right:

        tree[i] = nums[left]
        return tree[i]

    mid = (left+right) // 2

    tree[i] = segment(left, mid, i*2) + segment(mid+1, right, i*2+1)

    return tree[i]

# 구간 합
def search(start, end, left, right, i=1):

    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        return tree[i]

    mid = (start+end) // 2

    return search(start, mid, left, right, i*2) + search(mid+1, end, left, right, i*2+1)

def update(start, end, idx, diff, i=1):

    if start > idx or idx > end:
        return

    tree[i] += diff

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, diff, i*2)
        update(mid+1, end, idx, diff, i*2+1)

# n 수의 개수, m 수의 변경이 일어나는 횟수, k 구간의 합
n, m, k = map(int, input().split())

nums = [0] + [int(input()) for _ in range(n)]

tree = [0] * 2**(ceil(log(n, 2) + 2))
segment(0, n)

# print(tree)

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, n, b, (c-nums[b]))
        nums[b] = c

    else:
        print(search(0, n, b, c))

