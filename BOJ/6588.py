import sys

input = sys.stdin.readline

'''
1. input : while 문으로 number == 0 일때 멈춰!
2. 해당 숫자보다 작은 소수들의 모임을 만든다.
2-1. 2부터 시작해서 1000000 까지 중에 소수를 구한다.
2-2. 2의 배수 제거, 3의 배수 제거 ... 를 통해서 한다.
3. 소수들의 모임 젤 앞에 있는 숫자부터 차례대로 빼면서 해당 숫자가 있는지 없는지 구한다.
'''

# 소수 모임
sosu = [True] * 1000001
sosu[0] = False
sosu[1] = False
sosu[2] = False

for i in range(2, 1000001):
    for j in range(2, 1000001):
        num = i * j

        if num > 1000000:
            break

        sosu[num] = False


while True:

    number = int(input())

    if not number:
        break

    for i in range(3, 1000001):
        temp = number - i
        if temp < 0:
            print("Goldbach's conjecture is wrong.")
            break
        elif sosu[temp] and sosu[i]:
            print(number, "=", i, "+", temp)
            break





