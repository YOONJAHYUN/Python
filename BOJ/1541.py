import sys
input = sys.stdin.readline

def cal(data):

    ans = ''
    for char in data:

        if char in '+-':
            pass

        elif char in '()':
            pass

        else:
            ans += char

data = list(input().rstrip())
print(data)

# 숫자랑 연산자를 세트로 만들기
n = len(data)
ans = ''
for i in range(n):
    char = data[i]
    if char in '+-':
        if '(' in ans:
            ans += ')'
        ans += char
        ans += '('

    else:
        ans += char
        if i == n-1:
            ans += ')'

print(ans)

cal(ans)
