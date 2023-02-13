import sys

sys.stdin = open('input.txt')

# 정류장은 1번부터 1000번
# A에서 B는 무조건 정차
# 일반버스는 모두
# 급행버스는 A가 짝수인경우 A와 B 사이의 모든 짝수 번호에 정차, 홀수인경우 A와 B 사이의 모든 홀수
# 광역 급행버스 A 짝수인경우 A와 B 사이의 모든 4의 배수, A가 홀수인 경우 A와 B사이의 3의 배수이면서 10의배수가 아닌 번호

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stop = [0]*1001
    for n in range(N):
        bus, A, B = map(int, input().split())

        if bus == 1:
            for i in range(A, B+1):
                stop[i] += 1

        elif bus == 2:
            stop[A] += 1
            stop[B] += 1

            if A % 2 == 0:
                for i in range(A+1, B):
                    if i % 2 == 0:
                        stop[i] += 1

            else:
                for i in range(A+1, B):
                    if i % 2:
                        stop[i] += 1
        else:
            stop[A] += 1
            stop[B] += 1

            if A % 2 == 0:
                for i in range(A+1, B):
                    if i % 4 == 0:
                        stop[i] += 1
            else:
                for i in range(A+1, B):
                    if i % 3 == 0 and i % 10:
                        stop[i] += 1

    print(f'#{tc}', max(stop))

