T = int(input())

for i in range(T):

    N = int(input())

    bus = []

    for j in range(N):
        
        no, A, B = map(int, input().split())

        # 일반버스
        if no == 1:
            bus += list(range(A, B+1))
        
        # 급행버스
        if no == 2:
            bus += list(range(A, B+1, 2)) #홀수, 짝수 상관없이 2칸씩 

        if no == 3:
            if A % 4 == 0:
                bus += list(range(A, B+1, 4))
            else:
                bus += list(range((A//4 +1)* 4, B+1, 4))

        print(bus)
    # count = 0
    # for k in range(len(bus)):
    #     if count < bus.count(bus[k]):
    #         count = bus.count(bus[k])

    # print(f'#{i+1} {count}')

# # print(bus)