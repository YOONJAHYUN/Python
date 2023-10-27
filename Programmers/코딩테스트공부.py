import sys

sys.setrecursionlimit(10 ** 7)

import sys

sys.setrecursionlimit(10 ** 7)


def solution(alp, cop, problems):
    answer = 151
    max_alp, max_cop = 0, 0

    def check(alp, cop, time):
        nonlocal answer, max_alp, max_cop
        if time >= answer:
            return

        if alp >= max_alp and cop >= max_cop:
            # print(time)
            answer = min(time, answer)
            return

        #         if alp > max_alp:
        #             return

        #         if cop > max_cop:
        #             return

        for i in range(len(problems)):
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]

            if alp >= alp_req and cop >= cop_req:
                check(alp + alp_rwd, cop + cop_rwd, time + cost)

            else:
                break

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    problems.sort(key=lambda x: (x[0] + x[1], x[0], x[1], -x[2], -x[3]))

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    # print(max_alp, max_cop)
    check(alp, cop, 0)
    return answer

solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])