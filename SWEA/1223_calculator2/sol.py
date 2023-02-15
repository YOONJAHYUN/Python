import sys

sys.stdin = open('input.txt')

def postfix(cal): # 후위표기식으로 만들기
    stack = []
    result = ''
    for char in cal:
        if char in '/*-+':
            if char in '+-':
                while stack:
                    result += stack.pop()
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)

        else:
            result += char
    else:
        while stack:
            result += stack.pop()
    return result

def calculator(cal):

    stack = []

    for char in cal:
        if char in '/*-+':
            a = int(stack.pop())
            b = int(stack.pop())
            if char == '+':
                stack.append(b+a)
            elif char == '-':
                stack.append(b-a)
            elif char == '*':
                stack.append(b*a)
            elif char == '/':
                stack.append(b/a)

        else:
            stack.append(int(char))
    return stack.pop()





for tc in range(1, 11):
    n = int(input())
    cal = list(input())
    calculator(postfix(cal))
    # print(f'#{tc}', postfix(cal))
    print(f'#{tc}', calculator(postfix(cal)))


