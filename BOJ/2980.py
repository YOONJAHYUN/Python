import sys

input = sys.stdin.readline

# N 신호동의 개수, L 도로의길이
N, L = map(int, input().split())

wait = 0
for _ in range(N):
    # D는 신호동의 위치
    # R 빨간색 지속 시간
    # G 초록색 지속 시간
    D, R, G = map(int, input().split())

    # 내가 지나가는 시간은 지금까지 기다린 시간과 D를 더한 값

    # 기다려야하는 시간을 구해야한다.
    waiting_time = R-((D+wait) % (G+R))
    if waiting_time > 0:

        wait += waiting_time

print(wait+L)
