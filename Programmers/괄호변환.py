from collections import deque

answer = deque()


def check(p):
    global answer
    # 입력값이 ''라면 return
    if not p:
        return

    # u와 v를 분리한다.
    # for 문을 돌려서 u에 스택처럼 쌓는다. 괄호 끝나면 u랑 v랑 나누기
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
    check(v)
    # print("시이이이작")
    # print('u',u, 'v',v)
    # print()
    # return된 위치에서 4번조건 시작
    # u가 올바른지 아닌지 조사
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

    # u가 올바른 문자열이 아닌경우
    result = ''
    if not flag:
        print(u, "실패")
        new_u = u[1:len(u) - 1:-1]
        result += '('
        result += v
        result += ')'
        result += new_u
        # print('최종1',result)

        answer.appendleft(result)
        return
    # u가 올바른 문자열일경우
    # print("최종",u+v)
    answer.appendleft(u)
    return


def solution(p):
    global answer
    # answer = ''
    check(p)
    answer = ''.join(list(answer))
    return answer