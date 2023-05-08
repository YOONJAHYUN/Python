def solution(expression):
    answer = 0
    # 수식 우선순위를 먼저 정한다.
    # 우선 순위 하나씩 숫자 계산..

    cal = [["+", "-", '*'], ["+", "*", '-'], ["-", "+", '*'], ["-", "*", '+'], ["*", "-", '+'], ["*", "+", '-']]

    for signs in cal:
        temp1 = expression.split(signs[0])
        temp2 = []
        for j in temp1:
            temp2.append(j.split(signs[1]))
        # print(temp1)
        # print(temp2)
        for i in range(len(temp2)):
            for j in range(len(temp2[i])):
                temp2[i][j] = str(eval(temp2[i][j]))
        # print(temp2)

        for i in range(len(temp2)):
            if len(temp2[i]) >= 2:
                temp2[i] = [str(eval(signs[1].join(temp2[i])))]

        # print(temp2)
        ans = ''
        for i in range(len(temp2)):
            for j in range(len(temp2[i])):
                ans += temp2[i][j]
            if i != len(temp2) - 1:
                ans += signs[0]

        # print(ans)

        ans = eval(ans)
        if ans < 0:
            # print("음수",ans)
            answer = max(-ans, answer)
            # print(answer)
        else:
            answer = max(ans, answer)
        # print()
    return answer