import sys
input = sys.stdin.readline

data = list(input().rstrip())
n = len(data)
stack = []
idx = []
result = []

# 괄호쌍들을 짝지어서 묶어준다.
for i in range(n):
    if data[i] == '(':
        stack.append((i, data[i]))

    elif data[i] == ')':
        if stack[-1][1] == '(':
            index, gwal = stack.pop()
            idx.append((index, i))


# print(stack)
# print(idx)

# 부분집합을 구한다.
# 내가 구해보자... 어떻게 하더라..
N = len(idx)

bit = [0] * N

def f(depth, N, bit):
    global idx, data

    if depth == N:
        # print(bit)
        temp = data.copy()
        for i in range(N):
            if bit[i] == 0:
                for j in range(2):
                    temp[idx[i][j]] = ''
        result.append(temp.copy())
        return

    for i in range(2):
        bit[depth] = i
        f(depth+1, N, bit)


f(0, N, bit)
# print(stack)

ans = []
for i in range(len(result)):
    if result[i] == data:
        continue

    else:
        if "".join(result[i]) in ans:
            continue
        else:
            ans.append("".join(result[i]))
ans.sort()
for i in ans:
    print(i)


