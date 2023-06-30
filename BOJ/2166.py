import sys
input = sys.stdin.readline

n = int(input())

data = [tuple(map(int, input().split())) for _ in range(n)]

# 신발끈 공식
S = 0

for x, y in data:
