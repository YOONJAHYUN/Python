import sys
sys.stdin = open('input.txt')


def charge(start, end, cnt, rest):
    global result
    if start == end:
        if cnt != 0:

            result.append(cnt)
            # result = min(cnt, result)
        return

    if rest == 0:
        return


    # 다음 차례 안가기
    charge(start + 1, end, cnt, rest - 1)

    # 다음 차례 가기
    charge(start+1, end, cnt+1, rest+battery[start+1]-1)





# 최소한의 교체 횟수
T = int(input())

for tc in range(1, T+1):
    battery = list(map(int, input().split()))
    n = battery[0]
    result = []
    # result = 800
    charge(1, n-1, 0, battery[1])
    print(result)
    print(min(result))

