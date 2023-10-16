import sys

input = sys.stdin.readline

n = int(input())

'''
양수,
0 과 음수
나눠서 문제 풀기
'''
# 양수
data1 = []
# 0과 음수
data2 = []

for _ in range(n):
    number = int(input())
    if number > 0:
        data1.append(number)
    else:
        data2.append(number)

data1.sort(reverse=True)
data2.sort()

# print(data1)
# print(data2)

answer = 0
i = 0

while i < len(data1):

    if i+1 < len(data1) and data1[i] != 1 and data1[i+1] !=1:
        answer += data1[i] * data1[i+1]
        i += 2
    else:
        answer += data1[i]
        i += 1

# zero 여부

while data2 and data2[-1] == 0:

    if len(data2) % 2:
        data2.pop()
    else:
        data2.pop()
        data2.pop()

i = 0

while i < len(data2):

    if i+1 < len(data2):
        answer += data2[i] * data2[i+1]
        i += 2
    else:
        answer += data2[i]
        i += 1

print(answer)

