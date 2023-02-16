import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

num = list(range(1, n+1))
# print(num)
stack = []
# stack.append(num.pop(0))
result = ''
for number in numbers:
    if not stack:
        stack.append(num.pop(0))
        result += '+'

    # if not num:
    #     print('NO')
    #     break

    while stack and num:
        if number == stack[-1]:
            break
        stack.append(num.pop(0))
        result += '+'

    if stack and stack[-1] == number:
        stack.pop()
        result += '-'
else:
    if stack:
        print("NO")
    else:
        for i in result:
            print(i)


