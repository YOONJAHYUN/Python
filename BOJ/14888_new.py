import sys
input = sys.stdin.readline

def per(depth, n, ans, data, result):

    if depth == n:
        result.append(ans)
        return ans

    for i in range(n):
        num1 = numbers[0]

        if not selection[i]:
            selection[i] = True

            if data[i] == '+':
                num1 = num1 + num2

            elif data[i] == '-':
                num1 = num1 - num2

            elif data[i] == '*':
                num1 = num1 * num2

            else:
                if num1 < 0:
                    num1 = -(abs(num1) // num2)
                else:
                    num1 = num1 // num2

            per(depth+1, n, ans + [data[i]], data, result)
            selection[i] = False


N = int(input())
numbers = list(map(int, input().split()))
mul = list(map(int, input().split()))
ca = '+'*mul[0] + '-'*mul[1] + '*'*mul[2] + '/'*mul[3]
selection = [False] * N

ca_per = []

print(per(0, N-1, [], ca, ca_per))

my_max = -100000000
my_min = 100000000

for j in range(len(ca_per)):
    num1 = numbers[0]
    for i in range(1, N):
        num2 = numbers[i]
        if ca_per[j][i - 1] == '+':
            num1 = num1 + num2
        elif ca_per[j][i - 1] == '-':
            num1 = num1 - num2
        elif ca_per[j][i - 1] == '*':
            num1 = num1 * num2
        else:
            if num1 < 0:
                num1 = -(abs(num1)//num2)
            else:
                num1 = num1 // num2
    my_min = min(my_min, num1)
    my_max = max(my_max, num1)


print(my_max, my_min)


# for i in range(len(num_per)):
#     # print(ans)
#     for j in range(len(ca_per)):
#         num1 = num_per[i][0]
#         for k in range(0, N-1):
#             num2 = num_per[i][k+1]
#
#             if ca_per[j][k] == '+':
#                 num1 = num1 + num2
#             elif ca_per[j][k] == '-':
#                 num1 = num1 - num2
#             elif ca_per[j][k] == '*':
#                 num1 = num1 * num2
#             else:
#                 num1 = num1 // num2
#
#         if num1 < my_min:
#             my_min = num1
#             print(num_per[i], ca_per[j], num1)
#
#         if num1 > my_max:
#             my_max = num1
#
#
# print(my_max, my_min)

