# 괄호
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    gwalho = input().rstrip()

    stack = []

    for char in gwalho:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'NO'
                break
    else:
        if stack:
            result = 'NO'
        else:
            result = 'YES'

    print(result)