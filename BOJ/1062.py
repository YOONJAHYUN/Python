import sys
input = sys.stdin.readline
from itertools import combinations

# n 단어개수 k 가르칠 글자수
n, k = map(int, input().split())
words = [(input().rstrip()) for _ in range(n)]

base = set(['a','n','t','i','c'])

can = k - 5

if can < 0:
    print(0)
else:
    result = []
    for word in words:

        sett = set(word)
        temp = sett-base
        # if len(temp) <= can:
            # temp = list(temp)
        tmp = []
        for char in temp:
            tmp.append(ord(char)-ord('a')+1)
        result.append(tmp)

    # result에는 남는 애들이 다 모여있다.
    # 필수인자 빼고 남은 애들로 조합을 구하고 그 조합과 result를 순회하면서 비트마스킹
    # 최대값 갱신
    rest = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    my_cnt = 0
    for combi in combinations(rest, can):

        # 만들수있는 조합이 tmp안에 담겨있다 숫자형태로
        tmp = []
        for char in combi:
            tmp.append(ord(char)-ord('a')+1)

        for i in range(1<<can):
            cnt = 0
            for j in range(can):
                if i&(1<<j):
                    cnt += 1
            my_cnt = max(cnt, my_cnt)
    print(my_cnt)
