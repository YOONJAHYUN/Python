import sys
input = sys.stdin.readline

def get_numbers(n):
    global ans, result, stack

    # 제일 처음 숫자를 result에 넣는다.
    # 두번째 숫자는 for문을 돌려서 result에 넣는다.
    # 세번째 숫자는 result 첫번째와 두번째를 빼서 넣은거다.
    # 네번째 숫자는 result 두번째와 세번째를 빼서 넣은거다.

    for i in range(1, n):
        result.append(n)
        stack.append(n)
        result.append(i)
        stack.append(i)
        # print(stack)
        while True:

            a = stack.pop(0)
            b = stack[0]

            if a-b >= 0:
                result.append(a-b)
                stack.append(a-b)
            else:
                break

        if len(ans) < len(result):
            ans = result
        result = []
        stack = []



number = int(input())
result = []
stack = []

ans = []
get_numbers(number)

if number == 1:
    print(4)
    print(1, 1, 0, 1)
else:
    print(len(ans))
    print(*ans)