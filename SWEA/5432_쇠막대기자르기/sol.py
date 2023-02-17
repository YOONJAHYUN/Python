import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(input().rstrip())
    # print(data)
    gwalho = []
    stack = []
    cnt = [0, 0]
    # data를 순회하면서 ()있을 경우 양옆 ()를 없애준다.
    for char in data:
        stack.append(char)
        if char == '(':
            cnt[0] += 1

        else:
            cnt[1] += 1

            if cnt[0] == cnt[1]:
                gwalho.append(stack[::])
                stack.clear()
                cnt[0], cnt[1] = 0, 0

#####################################
    print(gwalho)

    gwal = []
    for lst in gwalho:
        for char in lst:
            if char == '(':
                gwal.append(char)
            else:
                if gwal[-1] == '(':
                    gwal.pop()
                else:

