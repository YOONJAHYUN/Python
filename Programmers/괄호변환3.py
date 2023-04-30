from collections import deque


def device(chars):
    # 문자열 p를 나눔
    chars = deque(chars)

    if not chars:
        return chars

    u = []
    cnt1 = 0
    cnt2 = 0
    for i in range(len(chars)):
        char = chars.popleft()
        if char == '(':
            u.append(char)
            cnt1 += 1
        else:
            u.append(char)
            cnt2 += 1

        if cnt1 == cnt2:
            break
    v = list(chars)
    # print('u',u, 'v', v)

    # 올바른 괄호 문자열인지 조사
    # 올바르다면
    if check(u):
        return u + list(device(v))
    else:
        result = ''
        result += '('
        for char in list(device(v)):
            result += char
        # result += list(device(v))
        result += ')'

        for i in range(1, len(u) - 1):
            if u[i] == '(':
                result += ')'
            else:
                result += '('
        return result


def check(u):
    flag = True
    stack = []

    for char in u:
        # (라면 넣고
        if char == '(':
            stack.append(char)
        # ) 라면 그전값이 (면 없애준다
        elif stack and stack[-1] == '(':
            stack.pop()
        # )만 있다면 올바른 괄호 문자열이 아님
        else:
            flag = False
            break

    return flag


def solution(p):
    answer = device(p)
    print(answer)
    return answer

solution(")(")