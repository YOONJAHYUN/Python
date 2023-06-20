import sys

input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().rstrip())

words.sort(key=lambda x:len(x))

dic = {}
for word in words:
    for i in range(len(word)):
        word[i]