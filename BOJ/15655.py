import sys
input = sys.stdin.readline

def NM(depth, i, idx):
    if depth == M:
        print(i.lstrip())
        return

    for j in range(idx, N):
        # 선택되어 있지 않은 걸 넣어야됨
        if not selection[j]:
            selection[j] = True
            # 어떻게 푼건지 모르겠음..?????
            NM(depth+1, i +' '+str(numbers[j]), idx+1)
            # 조합으로 구하는 것이기때문에 idx를 하나씩 증가시켜준다.
            idx += 1
            selection[j] = False



N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# 사전 순이므로 정렬
numbers.sort()

selection = [False] * N
NM(0, '', 0)
