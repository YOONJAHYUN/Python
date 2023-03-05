import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    data = [list(input().rstrip()) for _ in range(100)]
    # print(data[0][4:9])
    # print(data[0][9:4:-1])
    words = []
    long = 0
    data2 = list(zip(*data))

    # 가로부터 찾기
    for i in range(100):
        for j in range(100):
            for k in range(99, -1, -1):
                if data[i][j:k] and data[i][j:k] == data[i][k:j:-1]:
                    if len(data[i][j:k]) > long:
                        long = len(data[i][j:k])

                if data2[i][j:k] and data2[i][j:k] == data2[i][k:j:-1]:
                    if len(data2[i][j:k]) > long:
                        long = len(data[i][j:k])

    # 왜 +1 해야할까용.....
    print(f'#{tc}', long+1)
