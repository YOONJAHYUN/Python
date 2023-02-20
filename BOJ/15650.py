import sys
input = sys.stdin.readline

def f(n, m, depth = 0, i = 0, combi = []):
    if depth == m:
        print(*combi)
        return
    # 이전단계에서 뭘 받을건지부터..
    # 받아주는거랑 넘겨주는게 같아야한다.
    # 순회하고, i를 다음단계
    for j in range(i+1, n+1):
        combi.append(j)
        f(n, m, depth+1, j, combi)
        combi.pop()

N, M = map(int, input().split())

f(N, M)


