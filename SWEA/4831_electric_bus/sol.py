import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    stop = map(int, input().split())

    # 설치된 정류장 개수
    bus_line = [0] * (N+1)

    # 정류장에 설치된 충전기 위치 표시
    for i in stop:
        bus_line[i] += 1

    # K칸 이동시에 충전소가 있으면 okay, 없으면 한칸 전으로 찾기
    i = K
    count = 0
    charge_stop = []
    while True:
        if bus_line[i] == 1:
            count += 1
            charge_stop.append(i)
            i += K

        else:
            i -= 1

        if i >= N:
            print(f'#{tc+1}', count)
            break

        if i in charge_stop:
            print(f'#{tc+1}', 0)
            break

        if i == 0:
            print(f'#{tc+1}', 0)
            break
