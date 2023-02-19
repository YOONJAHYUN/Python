import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = list(input().rstrip())

    # print(data)
    stack =[]
    result = ''
    for char in data:
        if char == '+':
            while stack:
                result += stack.pop()
            stack.append(char)
        else:
            result += char
    else:
        if stack:
            result += stack.pop()
    # print(result)

    rsl = []
    for char in result:

        if char == '+':
            n1 = int(rsl.pop())
            n2 = int(rsl.pop())
            rsl.append(n2+n1)
        else:
            rsl.append(char)
    print(f'#{tc}', *rsl)