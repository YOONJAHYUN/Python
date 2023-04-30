def check(gems, s, e, n, ans):
    start = s
    end = e
    # print('***', ans)
    while end <= n:
        # print(start, end)
        candi = set()
        for i in range(start, end):
            candi.add(gems[i])
        # candi = list(candi)
        # candi.sort()
        # print(candi)

        if candi == ans:
            # print('####맞아용#######')
            # print(candi)
            # print(start+1, end)
            return (start + 1, end)

        start += 1
        end += 1
    return False


def solution(gems):
    answer = []

    n = len(gems)

    ans = set(gems)
    # ans = list(sett)
    # ans.sort()

    m = len(ans)

    start = 0
    end = m
    # print(check(gems, start, end, n, ans))

    while end <= n:

        res = check(gems, start, end, n, ans)

        if res:
            answer.append(res[0])
            answer.append(res[1])
            break

        start = 0
        end = m + 1

    return answer