import sys
sys.stdin = open('input.txt')

def work_hard(depth, n, percent):
    global selection
    global result

    # 모두 선택 된 경우 percent 반환
    if depth == n:
        result = max(result, percent)
        return

    if percent <= result:
        return

    for i in range(n):
        # 만약 선택된적이 없다면 이 친구를 선택
        if not selection[i]:
            # 선택 표시
            selection[i] = True
            work_hard(depth+1, n, float(percent*(work[depth][i]/100)))
            # 선택 해제
            selection[i] = False

T = int(input())

for tc in range(1, 1+T):

    N = int(input())

    work = []
    selection = [False]*N

    for _ in range(N):
        work.append(list(map(int, input().split())))
    # print(work)
    result = 0
    work_hard(0, N, 1)

    print(f'#{tc}', format(result*100, '6f'))
