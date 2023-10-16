def solution(info, query):
    answer = []

    candis = []
    for lst in info:
        candis.append(lst.split(" "))

    candis.sort()
    querys = []

    for condition in query:
        querys.append(condition.replace(" and", "").split(" "))

    for query in querys:
        cnt = 0
        for candi in candis:
            flag = True

            for i in range(4):

                if query[i] == '-':
                    continue

                if query[i] != candi[i]:
                    flag = False
                    break

            if flag and int(query[4]) <= int(candi[4]):
                cnt += 1

        answer.append(cnt)

    return answer