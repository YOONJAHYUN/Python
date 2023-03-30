import sys
sys.stdin = open('input.txt')

def binary(start, end, num, ans):
    global cnt

    mid = (start + end) // 2

    # 발견
    if num == N_data[mid]:
        cnt += 1
        return

    # 값이 mid보다 작으면 왼쪽
    elif num < N_data[mid]:
        if ans and ans[-1] == 0:
            return
        else:
            binary(start, mid-1, num, ans + [0])

    # 값이 mid보다 크면 오른쪽
    else:
        if ans and ans[-1] == 1:
            return
        else:
            binary(mid+1, end, num, ans+[1])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    N_data = list(map(int, input().split()))
    M_data = list(map(int, input().split()))

    N_data.sort()
    cnt = 0

    for num in M_data:

        # N데이터에 없는 경우
        if num not in N_data:
            continue

        # N데이터에 있는 경우
        else:
            binary(0, N-1, num, [])

    print(f'#{tc}', cnt)
