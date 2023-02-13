import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []

    for char in word:
        if char == '(' or char == '{':
            stack.append(char)

        elif char == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print(f'#{tc}', 0)
                    break

            else:
                print(f'#{tc}', 0)
                break

        elif char == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    print(f'#{tc}', 0)
                    break
            else:
                print(f'#{tc}', 0)
                break

    else:
        if stack:
            print(f'#{tc}', 0)
        else:
            print(f'#{tc}', 1)


