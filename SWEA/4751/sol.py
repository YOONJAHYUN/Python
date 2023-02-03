import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    word = input()
    word_len = len(word)
    arr = [['.'] * (word_len * 5 -(word_len-1)) for _ in range(5)]

    # print(arr)
    arr_len = len(arr[0])
    # for i in range(arr_len): # 5

    # 단어와 #을 같이 저장..?
    word_list = []
    for i in range(word_len):
        word_list.append('#')
        word_list.append('.')
        word_list.append(word[i])
        word_list.append('.')
        if i == (word_len -1):
            word_list.append('#')

    # print(word_list)

    for i in range(arr_len):
        arr[2][i] = word_list[i]

    for i in range(1, arr_len, 2):
        arr[1][i] = '#'
        arr[3][i] = '#'

    for i in range(2, arr_len, 4):
        arr[0][i] = '#'
        arr[4][i] = '#'

    for i in range(len(arr)):
        print(''.join(arr[i]))


