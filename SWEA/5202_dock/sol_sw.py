def dock(idx, s, e, cnt):
    global result

    if idx == N:
        result = max(result, cnt)
        return

    start, end = work[idx]
    if cnt == 0:
        dock(idx + 1, start, end, cnt + 1)
    elif not (s <= start < e):
        dock(idx + 1, s, end, cnt + 1)
    dock(idx + 1, s, e, cnt)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    work.sort()

    result = 0
    dock(0, 0, 0, 0)
    print(f'#{tc}', result)