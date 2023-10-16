import sys
input = sys.stdin.readline


# n 책 개수 m 최대 개수
n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
# print(data)

negative = []
positive = []


for i in range(n):

    if data[i] > 0:
        positive.extend(data[i:])
        break
    else:
        negative.append(data[i])

# print(negative)
# print(positive)
answer = 0

max_number = 0
cnt = 1
if positive and negative:
    max_number = max(positive[-1], abs(negative[0]))
    if max_number == positive[-1]:
        answer += positive.pop()
        while positive and cnt < m:
            positive.pop()
            cnt += 1

    else:
        answer -= negative.pop(0)
        while negative and cnt < m:
            negative.pop(0)
            cnt += 1

elif positive:
    max_number = positive[-1]
    answer += positive.pop()
    while positive and cnt < m:
        positive.pop()
        cnt += 1
else:
    max_number = abs(negative[0])
    answer -= negative.pop(0)
    while negative and cnt < m:
        negative.pop(0)
        cnt += 1

for i in range(len(positive)-1, -1, -m):
    answer += positive[i] * 2

for i in range(0, len(negative), m):
    answer -= negative[i] * 2

# print("#############3")
print(answer)
