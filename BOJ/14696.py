import sys

input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):

    # 4 별 3 동그라미 2 네모 1 세모

    # 그림의 개수, 무슨그림인지.
    a, *a_cards = map(int, input().split())
    b, *b_cards = map(int, input().split())

    a_card = [0, 0, 0, 0, 0]
    b_card = [0, 0, 0, 0, 0]
    for card in a_cards:
        a_card[card] += 1

    for card in b_cards:
        b_card[card] += 1

    if a_card[4] > b_card[4]:
        print('A')
    elif a_card[4] < b_card[4]:
        print('B')
    else:
        if a_card[3] > b_card[3]:
            print('A')
        elif a_card[3] < b_card[3]:
            print('B')
        else:
            if a_card[2] > b_card[2]:
                print('A')
            elif a_card[2] < b_card[2]:
                print('B')
            else:
                if a_card[1] > b_card[1]:
                    print('A')
                elif a_card[1] < b_card[1]:
                    print('B')
                else:
                    print('D')