import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(T):
    N = int(input())

    wordword = ''

    for i in range(N):
        char, num = input().split()
        num = int(num)

        word = char * num

        wordword += word

    print(f'#{tc+1}')
    for i in range(len(wordword)//10 + 1):
        print(wordword[i*10:10*(i+1)])