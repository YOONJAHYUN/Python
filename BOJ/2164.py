import sys
from collections import deque

input = sys.stdin.readline

k = int(input())

cards = deque(list(range(1, k+1)))
# print(cards)
while len(cards) > 1:

    cards.popleft()
    cards.append(cards.popleft())


print(*cards)
