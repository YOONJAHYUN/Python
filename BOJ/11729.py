import sys

input = sys.stdin.readline

def top(n, start, end):
    if n == 1:
        print(start, end)
    else:
        top(n-1, start, 6-end-start)
        print(start, end)
        top(n-1, 6-end-start, end)

# 원판의 개수
N = int(input())
print(2**N-1)
top(N, 1, 3)
