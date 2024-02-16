import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

numbers = [False] * (1000001)

for i in range(n):
    numbers[data[i]] = True

answer = [0] * 1000001
for i in range(1000001):
    # 해당 숫자가 존재한다면
    if numbers[i]:
        for j in range(i*2, 1000001, i):
            if numbers[j]:
                answer[j] -= 1
                answer[i] += 1

for i in range(n):
    print(answer[data[i]], end=" ")


