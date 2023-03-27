import sys
input = sys.stdin.readline

def hagisiro(depth, n, num):

    if depth == n:
        result.append(num)
        # print(num)
        return

    for i in range(n):
        num1 = num
        num2 = numbers[depth + 1]
        if not selection[i]:
            if ca[i] == '+':
                num1 = num1 + num2
            elif ca[i] == '-':
                num1 = num1 - num2
            elif ca[i] == '*':
                num1 = num1 * num2
            else:
                if num1 < 0:
                    num1 = -(abs(num1) // num2)
                else:
                    num1 = num1 // num2
            selection[i] = True
            hagisiro(depth+1, n, num1)
            selection[i] = False


N = int(input())
numbers = list(map(int, input().split()))
mul = list(map(int, input().split()))
ca = '+'*mul[0] + '-'*mul[1] + '*'*mul[2] + '/'*mul[3]
selection = [False] * (N-1)

result = []
hagisiro(0,N-1,numbers[0])

print(max(result),min(result))