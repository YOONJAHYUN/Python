import sys
sys.stdin = open('input.txt')
# 문제를 잘 읽자.... 충전이 아니라 충전지 교체이다..
def charge(start, end, cnt, rest):
    global ans

    # 목적지 도달 했을 때 cnt 값 주기
    if start == end and rest > 0:
        ans = min(ans, cnt)
        return

    # 만약에 남은 연료가 없으면 return
    if rest == 0:
        return

    # 이미 최솟값보다 크면 return
    if cnt >= ans:
        return

    # 다음 장소 간다
    # start -> 다음장소 cnt+1로 충전지 교체
    charge(start+1, end, cnt+1, battery[start])

    # 다음 장소 안간다.
    charge(start+1, end, cnt, rest-1)

# 최소한의 교체 횟수
T = int(input())

for tc in range(1, T+1):
    battery = list(map(int, input().split()))
    n = battery[0]
    ans = n
    charge(2, n, 0, battery[1])

    print(f'#{tc}', ans)
