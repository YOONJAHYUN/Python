import sys

sys.stdin = open('input.txt')

def no_jh(start, end, ans, target):
    global result
    if ans == target:
        result = 0
        return
    # 다 선택하고 해당 값을 result에 담기
    if start == end:
        if ans >= target:
            result = min(result, ans-target)

        return


    # 직원 뎃고가기
    no_jh(start+1, end, ans + data[start], target)
    # 직원 안데리고가기
    no_jh(start+1, end, ans, target)

T = int(input())

for tc in range(1, T+1):

    # N 직원 수 B 선반 높이
    N, B = map(int, input().split())
    data = list(map(int, input().split()))

    result = sum(data)
    no_jh(0, N, 0, B)
    print(f'#{tc}',result)
