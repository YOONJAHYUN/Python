import sys

sys.stdin = open('input.txt')

T = int(input())

# 정류장 5000개니까
for tc in range(T):
    stop = [0] * 5001
    N = int(input())
    for line in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            stop[i] += 1

    P = int(input())

    # 0번째는 없으니까 P개만 버스정류장을 만든다.

    # 버스 정류장을 input한다.
    aa = []
    for i in range(P):
        aa.append(int(input()))


    result = []
    for num in aa:
        result.append(stop[num])

    print(f'#{tc+1}', *result)