import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    numbers, count = map(str, input().split())
    count = int(count)
    # 0번과 그다음부터 젤 큰거랑 계속 차례대로 바꾼다.
    n = len(numbers)
    numbers = list(numbers)
    # max_numbers = sorted(numbers, reverse=True)
    # print(max_numbers)
    flag = False
    cnt = 0
    while not flag:

        for i in range(n):
            my_max = max(map(int, numbers[i:n]))
            for j in range(n-1, i, -1):
                if my_max >= int(numbers[i]) and my_max == int(numbers[j]):

                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    cnt += 1
                    if cnt == count:
                        flag = True
                        break
                    break

                elif my_max < int(numbers[i]):
                    break

            if flag:
                break

        if flag:
            break

        rest = count - cnt

        for i in range(rest):
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
            cnt += 1

        if cnt == count:

            break


    print(f'#{tc}', ''.join(numbers))

