import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    word = input()

    if len(word) == 1:
