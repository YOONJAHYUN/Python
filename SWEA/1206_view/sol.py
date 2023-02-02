import sys

sys.stdin = open('input.txt')

def min_num(n):
    minmin = n[0]
    for i in range(4):
        if n[i] < minmin:
            minmin = n[i]

    return minmin

for a in range(10):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 빌딩 양쪽 두개씩의 차이를 구하고 그 차이가 가장 적은거의 갯수를 세어보자
    building = 0
    for i in range(2, N-2):
        if ((numbers[i] - numbers[i-1]) >= 1) and ((numbers[i] - numbers[i-2]) >= 1) and ((numbers[i] - numbers[i+1]) >= 1) and ((numbers[i] - numbers[i+2]) >= 1):
            building += min_num([(numbers[i] - numbers[i-1]), (numbers[i] - numbers[i-2]), (numbers[i] - numbers[i+1]), (numbers[i] - numbers[i+2])])

    print(f'#{a+1} {building}')