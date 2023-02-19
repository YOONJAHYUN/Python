import sys
input = sys.stdin.readline

def f(n, m, depth):
    global num, combi

    if len(combi) == m:
        num.append(combi)

        return num

    # 순회하면서 select가 True면 다음단계
    for i in range(1, n+1):

        if select[i] == True:
            continue
        # 순회하는데 select가 False라면 True로 하고 다음 단계

        select[i] = True
        combi.append(i)
        f(n, m, depth+1)

        select[i] = False





N, M = map(int, input().split())
select = [False for _ in range(N+1)]
num = []
combi = []
f(N,M,0)
print(num)
