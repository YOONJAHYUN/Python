import sys

input = sys.stdin.readline

data = input().rstrip()

ans = ''
stack = []
for char in data:
    # 연산자
    if char in '+-*/()':
        # 우선순위 높은 순서대로
        if char in '()':
            if char == '(':
                stack.append(char)
            else:
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                # 마지막이 (일테니 없애주기
                stack.pop()

        elif char in '/*':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(char)
        # + -
        else:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(char)
    # 문자
    else:
        ans += char

while stack:
    ans += stack.pop()

print(ans)

'''
G*(A-B*(C/D+E)/F)

GABCD/E+*F/-*
'''