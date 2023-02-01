import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):

    N = int(input())

    bus_list = []

    for j in range(N):
        
        no, A, B = map(int, input().split())

        bus = []

        # 일반버스
        if no == 1:
            bus = list(range(A, B+1))
        
        # 급행버스
        if no == 2:
            bus = list(range(A, B+1, 2)) #홀수, 짝수 상관없이 2칸씩 
            
        # 광역 급행버스
        if no == 3:
            if A % 4 == 0:
                bus = list(range(A, B+1, 4))
            elif A % 4 == 1:
                bus = list(range(A+3, B+1, 4))
            elif A % 4 == 2:
                bus = list(range(A+2, B+1, 4))
            else:
                bus = list(range(A+1, B+1, 4))

        # 버스가 정차하는 곳 모두 한 리스트에 추가하기
        bus_list += bus

    # 같은 정류장을 세고 최댓값 반환
    count = 0
    for k in range(len(bus_list)):
        bus_list.count(bus_list[k])

        if count < bus_list.count(bus_list[k]):
            count = bus_list.count(bus_list[k])

    print(f'#{i+1} {count}')