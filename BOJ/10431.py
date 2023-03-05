import sys

input = sys.stdin.readline

P = int(input())

for _ in range(P):

    T, *data = map(int, input().split())
    cnt = 0

    for i in range(20):
        for j in range(i):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
                cnt += 1



    print(T, cnt)