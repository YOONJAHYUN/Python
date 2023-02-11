# 좌표 정렬하기
import sys

input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    a, b = map(int, input().split())
    num.append((a,b))

num.sort(key=lambda x: (x[0], x[1]))
for i in num:
    print(*i)
    