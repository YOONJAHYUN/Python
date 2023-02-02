# 리스트 만들고 counting sorts에서 쓰는 것처럼 버스 정류장 number 숫자 세기

T = int(input())

for tc in range(T):

    N = int(input())

    # 정류장이 1000번까지 있으므로 1001으로 지정
    bus = [0] * 1001

    for j in range(N):
        
        no, A, B = map(int, input().split())

        # A와 B에는 항상 정차한다.
        bus[A] += 1
        bus[B] += 1

        # 일반버스
        if no == 1:
            for i in range(A+1, B):
                bus[i] += 1
        
        # 급행버스
        if no == 2:
            for i in range(A, B, 2):
                if i == A:
                    continue 
                bus[i] += 1

        # 광역 급행 버스        
        if no == 3:
            if A % 2: # 홀수인 경우
                for i in range(A+1, B): # A+1에서 B-1까지 순회하면서 3의배수와 10의 배수가 아닌 정류장을 찾는다.
                    if i % 10 != 0 and i % 3 == 0:
                        bus[i] += 1

            else: # 짝수인 경우
                for i in range(A+1, B):
                    if i % 4 == 0:
                        bus[i] += 1

    print(f'#{tc+1}', max(bus))