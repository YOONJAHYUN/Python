from collections import deque

answer = deque()


def gwal(u, v):
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

    result = ''

    # u가 올바르다면
    if flag:
        # v에 대해 다시
        check(v)
    # 올바르지 않아
    else:
        tmp = ''


def check(p):
    global answer
    # 입력값이 ''라면 return
    if not p:
        return p

    cnt1 = 0
    cnt2 = 0
    q = deque(p)
    u = ''
    while q:
        char = q.popleft()
        if char == '(':
            cnt1 += 1
            u += char
        else:
            cnt2 += 1
            u += char
        if cnt1 == cnt2:
            break
    # v는 남은 stack
    v = ''.join(list(q))
    # 남은 v도 돌려줌
    # print(u, v)
    gwal(u, v)

    # print('u', u)
    # print('v', v)
    # return 되고나서 괄호를 올바르게 배열


def solution(p):
    check(p)
    # answer = ''
    # return answer