import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

my_number = 1
result1 = []
result2 = []
for i in range(N-1):
    if data[i] <= data[i+1]:
        result1.append(data[i])
        if i == N-2:
            result1.append(data[i+1])
            my_number = max(len(result1), my_number)
    else:
        result1.append(data[i])
        my_number = max(len(result1), my_number)
        result1 =[]

    if data[i] >= data[i+1]:
        result2.append(data[i])
        if i == N-2:
            result2.append(data[i+1])
            my_number = max(len(result2), my_number)
    else:
        result2.append(data[i])
        my_number = max(len(result2), my_number)
        result2 =[]
print(my_number)