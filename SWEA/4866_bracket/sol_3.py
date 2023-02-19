import sys

sys.stdin = open('input.txt')

def f(data):
    stack = []
    for char in data:
        if char in '{}()':
            if char in '{(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return 0
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
        else:
            continue
    else:
        if stack:
            return 0
        else:
            return 1

T = int(input())

for tc in range(1, T+1):
    data = list(input().rstrip())

    print(f'#{tc}', f(data))