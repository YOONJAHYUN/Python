def solution(info, query):
    answer = []
    dict = {}

    for i in range(len(info)):

        for j in info[i].split(" "):
            if dict.get(j):
                dict[j].add(i)
            else:
                dict[j] = {i}
    # print(dict)

    for q in query:
        q = q.split(" ")
        # print(q)

        idx = 0
        now = {i for i in range(len(info))}
        # print(now)

        while idx < 7:
            if (q[idx] == "and"):
                idx += 1
            elif q[idx] == "-":
                idx += 2
            else:
                now = dict[q[idx]] & now
                idx += 2
        # print("최종", now)

        cnt = 0
        for i in now:
            if int(info[i].split(" ")[-1]) >= int(q[-1]):
                cnt += 1

        answer.append(cnt)
    return answer