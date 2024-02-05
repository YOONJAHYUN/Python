import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    indegree = [0] * (n+1)
    new_indegree = [0] * (n+1)
    data = list(map(int, input().split()))
    for i in range(n):
        indegree[data[i]] += i

    m = int(input())

    dict = {}
    for _ in range(m):
        a, b = map(int, input().split())
        dict[(a, b)] = 1

    for i in range(1, n+1):
        # new_indegree[i] += 1
        for j in range(i+1, n+1):
            # 만약 위상정렬이 바뀐다면?
            if dict.get((i, j)):
                # 차수 높은거에 낮은거 넣기 (위상정렬이 변경됐으니까)
                if indegree[i] > indegree[j]:
                    new_indegree[j] += 1
                else:
                    new_indegree[i] += 1

            # 위상정렬이 안바뀐다면? 그대로넣기
            elif indegree[i] < indegree[j]:
                new_indegree[j] += 1
            else:
                new_indegree[i] += 1


    # 불가능한 경우
    if sorted(new_indegree[1:]) != [i for i in range(n)]:
        print("IMPOSSIBLE")
    else:
        result = [0] * n
        for i in range(1, n+1):
            result[new_indegree[i]] = i
        print(*result)




