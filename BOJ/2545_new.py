import sys

input = sys.stdin.readline

T = int(input().rstrip())

# A B C가 최대한 비슷해야함
for i in range(T): 
    blank = input()

    A, B, C, D = map(int, input().rstrip().split())
    # A,B,C 정렬
    A, B, C = sorted((A, B, C))
    # A B C에 횟수를 빼고
    S = A + B + C - D
    # 뺀 값에서 가장 큰 값인 A와 비교해 더 작은 수를 A1으로 대입한다.
    tmp = min(S // 3, A)

    A1 = tmp
    # A 할당하고 나머지 B와 C로 나눔
    S -= tmp
    tmp = min(S // 2, B)
    
    print(A1 * tmp * (S - tmp))