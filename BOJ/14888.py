import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
multi = list(map(int, input().split()))
lst = []
for i in range(4):
    for j in range(multi[i]):

        if i == 0:
            lst.append('+')
        elif i == 1:
            lst.append(multi[i]*'-')
        elif i == 2:
            lst.append(multi[i]*'*')
        else:
            lst.append(multi[i]*'/')

if len(lst) == 1:
    per = lst
else:
    per = list(permutations(lst, N-1))

print(per)

my_max = -1000000000
my_min = 1000000000

result = []
result.append(numbers[0])
result.append(numbers[1])

for i in range(N-1):





print(my_max)
print(my_min)