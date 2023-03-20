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
            # 조합으로 구하는 것이기때문에 idx에 다음 값을 추가해준다.
            NM(depth+1, i +' '+str(numbers[j]), j+1)

            selection[j] = False



N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# 사전 순이므로 정렬
numbers.sort()

selection = [False] * N
NM(0, '', 0)
