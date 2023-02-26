import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

line = []

student = 1
for num in data:
    line.insert(num, student)
    student += 1


print(*line[::-1])
