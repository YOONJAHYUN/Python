import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    # print(word)

    # 최종 결괏값
    result = 1
    stack = []
    for char in word:

        if char == '(' or char == '{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack: # stack이 비었는데
                    result = 0
                    # 더 이상 조사 할 필요 없다.
                    break
                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
    if stack:
        result = 0

    print(f'#{tc}', result)