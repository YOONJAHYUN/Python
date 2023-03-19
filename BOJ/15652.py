import sys

input = sys.stdin.readline

def NM(depth, i, idx):
    if depth == M:
        print(i.lstrip())
        return
    # range start값을 바꿔줘야한다.
    # 바꾸는 값은 애초에 선택됐던 j값 그대로 가야해서 새로운 변수를 만들어 j를 할당한다.
    for j in range(idx, N+1):
        idx = j
        NM(depth+1, i + ' ' + str(j), idx)

N, M = map(int, input().split())
# 첫시작은 j == 1이기때문에 1로준다.
NM(0, '', 1)

