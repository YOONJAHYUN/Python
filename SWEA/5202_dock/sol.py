import sys
sys.stdin = open('input.txt')

def dock(depth, hour, cnt):
    global result

    if depth == N:
        result = max(result, cnt)
        # print(cnt)
        return

    for i in range(depth, N):
        # 방문기록이 없다면
        if not selection[i]:
            s, e = work[i]

            # 시간대에 하나라도 있다면 return
            for j in range(s, e):
                if j in hour:
                    selection[i] = True
                    dock(depth + 1, hour, cnt)
                    # selection[i] = False

                    return

            # 시간대에 비어있다면 등록해준다.
            else:
                # temp = list(range(s, e))

                selection[i] = True
                dock(depth+1, hour+list(range(s, e)), cnt+1)
                # selection[i] = False

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # work = []
    # for _ in range(N):
    #     work.append(list(map(int, input().split())))
    work = [list(map(int, input().split())) for _ in range(N)]
    work.sort(key=lambda x : x[1]-x[0])
    selection = [False] * N
    result = 0
    dock(0, [], 0)
    print(f'#{tc}', result)

