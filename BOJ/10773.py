# 제로
import sys

input = sys.stdin.readline

K = int(input())

numbers = []
for _ in range(K):
    numbers.append(int(input()))
stack = []
for char in numbers:
    if char == 0:
        stack.pop()
    else:
        stack.append(char)

print(sum(stack))
