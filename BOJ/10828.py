import sys

input = sys.stdin.readline

N = int(input())

stack = []

for n in range(N):
    a, *b = input().split()
    # b = int(b)


    if a == 'push':
        stack.append(int(*b))
    elif a == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif a == 'size':
        print(len(stack))
    elif a == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif a == 'top':
        if stack:
            print(int(stack[-1]))
        else:
            print(-1)