import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
multi = list(map(int, input().split()))
lst = multi[0]*'+' + multi[1]*'-' + multi[2]*'*'+ multi[3]*'/'

per = list(permutations(lst, N-1))

my_max = -1000000000
my_min = 1000000000

for i in range(len(per)):
    ans = 0
    num1 = numbers[0]
    num2 = numbers[1]
    for j in range(N-1):
        if j == 0:
            if per[i][j] == '+':
                ans = num1 + num2
            elif per[i][j] == '-':
                ans = num1 - num2
            elif per[i][j] == '*':
                ans = num1 * num2
            elif per[i][j] == '/':
                ans = int(num1 / num2)
        else:
            num = numbers[j+1]
            if per[i][j] == '+':
                ans = ans + num
            elif per[i][j] == '-':
                ans = ans - num
            elif per[i][j] == '*':
                ans = ans * num
            elif per[i][j] == '/':
                ans = int(ans / num)


    if ans > my_max:
        my_max = ans

    if ans < my_min:
        my_min = ans

print(my_max)
print(my_min)