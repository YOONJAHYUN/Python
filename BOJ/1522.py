import sys

input = sys.stdin.readline

word = input().rstrip()
answer = 1e9
countA = word.count('a')

left = 0

while left < len(word):
    right = left + countA

    if right > len(word):
        temp = word[left:len(word)] + word[:right-len(word)]

    else:
        temp = word[left:right]

    answer = min(answer, temp.count('b'))
    left += 1

print(answer)
