import sys
input = sys.stdin.readline

def f(n, m, depth):
    global num, combi

    if depth == m:
        if len(combi) == m:
            num.append(combi)

        return

    # 순회하고, i를 다음단계
    for i in range(1, n+1):


        combi.append(i)

        f(n, m, depth+1)

        combi = []

N, M = map(int, input().split())

num = []
combi = []
f(N,M,0)
print(num)
