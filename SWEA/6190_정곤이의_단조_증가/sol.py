import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    danjo_hubo = []
    for i in range(N):
        for j in range(i+1, N):
            danjo_hubo.append(numbers[i] *numbers[j])

    danjo = -1
    for num in list(map(str, danjo_hubo)):
        # print(num, type(num))
        for i in range(len(num)-1):
            # print(num[i])
            if num[i+1] < num[i]:
                break
        else:
            danjo = max(int(num), danjo)

    print(f'#{tc}', danjo)
