def solution(gems):
    now = []
    answer = []
    result = []

    sett = list(set(gems))
    # print(sett)

    n = len(gems)

    for i in range(n):
        if gems[i] not in answer:
            answer.append(gems[i])
            result.append(i)

        else:

            idx = answer.index(gems[i])
            answer.pop(idx)
            result.pop(idx)
            answer.append(gems[i])
            result.append(i)

        if list(set(answer)) == sett:
            print('일치', result)
            now.append(result[::])
            print(now)

    # print(answer)
    # print(result)
    print('####', now)
    # res = []
    # my_len = 100001
    # for lst in final:
    #     print(lst)
    # if len(lst) < my_len:
    #     my_len = lst
    #     res = [result[0]+1, result[-1]+1]

    # return res
solution(["AA", "AB", "AC", "AA", "AC"])