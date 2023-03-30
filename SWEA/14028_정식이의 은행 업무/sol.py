import sys
sys.stdin = open('input.txt')


def insik(num1, num2):
    num1 = list(num1)
    num2 = list(num2)

    result1 = []

    for i in range(len(num1)):
        # 1인 경우
        if num1[i] == '1':
            num1[i] = '0'

            # 2진법으로 바꾸기
            numbers = ''.join(num for num in num1)
            result1.append(int(numbers, 2))
            num1[i] = '1'
        # 0인 경우
        else:
            num1[i] = '1'
            numbers = ''.join(num for num in num1)
            result1.append(int(numbers, 2))
            num1[i] = '0'

    for i in range(len(num2)):
        # 0인 경우
        if num2[i] == '0':
            num2[i] = '1'

            # 3진법으로 바꾸기
            numbers = ''.join(num for num in num2)

            if int(numbers, 3) in result1:
                return int(numbers, 3)

            num2[i] = '2'
            numbers = ''.join(num for num in num2)
            if int(numbers, 3) in result1:
                return int(numbers, 3)

            num2[i] = '0'

        # 1인 경우
        elif num2[i] == '1':
            num2[i] = '0'

            # 3진법으로 바꾸기
            numbers = ''.join(num for num in num2)
            if int(numbers, 3) in result1:
                return int(numbers, 3)

            num2[i] = '2'
            numbers = ''.join(num for num in num2)
            if int(numbers, 3) in result1:
                return int(numbers, 3)
            num2[i] = '1'

        # 2인경우
        else:
            num2[i] = '1'
            # 3진법으로 바꾸기
            numbers = ''.join(num for num in num2)

            if int(numbers, 3) in result1:
                return int(numbers, 3)

            num2[i] = '0'

            numbers = ''.join(num for num in num2)
            if int(numbers, 3) in result1:
                return int(numbers, 3)

            num2[i] = '2'


# 한 자리씩 다른 숫자로 바꾸기
T = int(input())

for tc in range(1, 1+T):
    num1 = str(input())
    num2 = str(input())
    print(f'#{tc}',insik(num1,num2))


