import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    # 구간의 최소 길이가 1이므로 count = 1을 디폴트로 해준다.
    max_count = 1
    count = 1
    # i-1 값과 비교하기때문에 range를 1부터 시작한다.
    for i in range(1, N):
        # 만약에 연속한다면 count에 1을 더해준다.
        if C[i] == C[i-1] + 1:
            count += 1
            max_count = count
        # 만약에 연속하지 않는다면 count를 1로 초기화 시켜주고 원래 있던 count를 새로 max_count에 넣어준다.
        else:
            count = 1


    print(f'#{tc+1}', max_count)



