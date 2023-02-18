import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    data = list(map(int, input().split()))
    result = 0
    max_price = max(data)

    while data:
        # max인 날을 지정한다.
        one_day = data.pop(0)

        if one_day < max_price:
            result += (max_price - one_day)
        else:
            if data:
                max_price = max(data)
    print(f'#{tc}', result)
