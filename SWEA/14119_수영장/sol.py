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

    for option in range(4):

        # 하루권 선택
        if option == 0:
            cheap(start+1, end, money+price[option]*data[start])

        # 한달권
        elif option == 1:
            # 한달에 하루라도 가면
            if data[start] > 0:
                cheap(start+1, end, money+price[option])
            # 하루라도 안가면 구매하지 않는 것과 같다.
            else:
                cheap(start+1, end, money)

        # 3달권
        # 11월 이후부터는 구매는 가능하지만 이용가능 날짜가 달라짐 -> 종료조건을 수정

        elif option == 2:
            cheap(start + 3, end, money + price[option])


        # 1년 이용권 선택
        else:
            # 1월에만 구매 가능
            if start == 0:
                # 바로 마지막달로 이동
                cheap(start+12, end, money+price[option])
            else:
                return

T = int(input())

for tc in range(1, 1+T):

    price = list(map(int, input().split()))

    data = list(map(int, input().split()))
    result = 3000*12
    cheap(0, 12, 0)
    print(f'#{tc}', result)

