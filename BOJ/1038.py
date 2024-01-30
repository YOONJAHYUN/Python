import sys
input = sys.stdin.readline

n = int(input())

q = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while q:

    num = q.pop()

    for i in range(int(str(num)[-1])):
        new = int(str(num)+str(i))
        lst.append(new)
        q.append(new)


lst.sort()

try:
    print(lst[n])
except:
    print(-1)