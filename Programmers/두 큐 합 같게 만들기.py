from collections import deque


def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    my_sum = sum(queue1) + sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    if my_sum % 2:
        answer = -1
    else:
        cnt = 0
        while cnt <= n * 4:

            if sum(q1) == sum(q2):
                print(q1)
                break

            if sum(q1) > sum(q2):
                num1 = q1.popleft()
                q2.append(num1)
                cnt += 1

            else:
                num2 = q2.popleft()
                q1.append(num2)
                cnt += 1
            print(q1, q2, cnt)

        if cnt >= len(q1) * 4:
            answer = -1
        else:
            answer = cnt

    return answer

solution([1, 2, 1, 2], [1, 10, 1, 2])