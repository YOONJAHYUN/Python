import sys

input = sys.stdin.readline


N = int(input().rstrip())

numbers = []
for i in range(N):
    numbers.append(int(input().rstrip()))

numbers.sort()

for num in numbers:
    print(num)