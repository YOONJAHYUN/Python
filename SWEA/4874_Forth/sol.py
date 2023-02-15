import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(input().split())
    stack = []

    for char in data:
        if char in '/*-+':
            try:
                if char == '+':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b+a)

                elif char == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)

                elif char == '*':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b * a)

                elif char == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    # //로 해야됨 ^_^ / 하면 오류남 ;;;;ㅋ
                    stack.append(b // a)

            except: # 걍 쓰지마.....친구야....알겟지..?
                print(f'#{tc}', 'error')
                break

        else:
            if char == '.':
                a = stack.pop()
                if stack:
                    print(f'#{tc}', 'error')
                    break
                else:
                    print(f'#{tc}', a)
            else:
                stack.append(char)

