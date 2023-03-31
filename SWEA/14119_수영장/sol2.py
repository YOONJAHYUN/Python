import sys

sys.stdin = open('input.txt')

'''
1일 이용권
1달 이용권
3달 이용권
1년 이용권
'''

def cheap(start, end,money):
    global result

    if start >= end:
        # result.append(money)
        result = min(result, money)
        return

    if money >= result:
        return


    cheap(start + 1, end, money + price[0] * data[start])

    if data[start] > 0:
        cheap(start + 1, end, money + price[1])

    # 하루라도 안가면 구매하지 않는 것과 같다.
    else:
        cheap(start + 1, end, money)

    cheap(start + 3, end, money + price[2])

    cheap(start+12, end, money+price[3])

T = int(input())

for tc in range(1, 1+T):

    price = list(map(int, input().split()))

    data = list(map(int, input().split()))
    result = 3000*12
    cheap(0, 12, 0)
    print(f'#{tc}', result)

