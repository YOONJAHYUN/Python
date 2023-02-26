import sys

input = sys.stdin.readline

# 학생 수, 최대인원 수
N, K = map(int, input().split())

girl = [0] * 7
boy = [0] * 7

for _ in range(N):
    # 성별, 학년
    s, grade = map(int, input().split())
    # 여학생
    if s == 0:
        girl[grade] += 1

    else:
        boy[grade] += 1


result = 0
for num in girl:

    while num > K:

        result += 1
        num = num - K

    else:
        if num > 0:
            result += 1

for num in boy:

    while num > K:

        result += 1
        num = num - K

    else:
        if num >0:
            result += 1

print(result)
