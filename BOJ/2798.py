import sys

input = sys.stdin.readline

N, M = map(int,input().split())
cards = list(map(int, input().split()))
my_card = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] <= M:
                my_card.append(cards[i] + cards[j] + cards[k])

print(max(my_card))
