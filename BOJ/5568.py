import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())
k = int(input())

cards = []

for _ in range(n):
    cards.append(int(input()))

combi = list(permutations(cards, k))

# print(combi)
numbers = []
for i in range(len(combi)):
    number = ''
    for j in range(k):
        number += str(combi[i][j])
    if number not in numbers:
        numbers.append(number)

print(len(numbers))


