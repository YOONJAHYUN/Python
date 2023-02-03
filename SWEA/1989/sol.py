import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(T):
    word = input()
    re_word = ''
    for i in range(len(word)-1, -1, -1):
        re_word += word[i]


    if re_word == word:
        print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)
