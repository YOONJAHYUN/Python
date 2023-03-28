import sys

input = sys.stdin.readline

data = list(input().rstrip())
# print(data)

numbers = []
mul = []
ans = ''
for char in data:
    if char in '+-':
        numbers.append(int(ans))
        ans = ''
        mul.append(char)

    else:
        ans += char

numbers.append(int(ans))

print(numbers)
print(mul)




