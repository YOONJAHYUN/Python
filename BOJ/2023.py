import sys

input = sys.stdin.readline

def check(num):

    if len(str(num)) == n:
        print(num)
        return

    for i in range(1, 10):
        number = int(str(num) + str(i))

        temp = 2
        while temp < number:
            if number % temp == 0:
                # 소수아님
                break
            temp += 1
        else:


            check(number)

n = int(input())


for num in [2, 3, 5, 7]:
    check(num)

