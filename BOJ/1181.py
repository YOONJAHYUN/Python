import sys

input = sys.stdin.readline


N = int(input().rstrip())

words = []
for i in range(N):
    words.append(input().rstrip())

words.sort(key=lambda x: (len(x), x))

words_list = []
for word in words:
    if word not in words_list:
        words_list.append(word)
        print(word)