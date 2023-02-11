import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]

    count = 0
    for i in range(8):
        for j in range(9-n):
            word1 = ''
            word2 = ''
            for k in range(n):
                word1 += arr[i][j+k]
                word2 += arr[j+k][i]
            if word1 == word1[::-1]:
                count += 1
            if word2 == word2[::-1]:
                count += 1

    print(f'#{tc}', count)

