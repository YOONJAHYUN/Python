import sys

input = sys.stdin.readline

N = int(input())

def stack(a, b=-1):
    lst = []
    if a == 'push':
        lst.append(b)
    elif a == 'top':
        if len(lst) == 0:
            print(-1)
        print(lst[-1])
    elif a == 'size':
        print(len(lst))
    elif a == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    elif a == 'pop':
        if stack:
            print(lst[-1])
            lst.remove(-1)
        else:
            print('1')


for n in range(N):
    a, b = input().split()
    b = int(b)
    print(stack(a, b))