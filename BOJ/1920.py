import sys

input = sys.stdin.readline

N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

for i in range(M):
    if list_M[i] in list_N:
        print(1)
    else:
        print(0)