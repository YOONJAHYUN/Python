import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = input()
    stack = []
    for char in words:
        if stack:
            if stack[-1] == char:
                stack.pop(-1)
            else:
                stack.append(char)
        else:
            stack.append(char)

    print(f'#{tc}', len(stack))