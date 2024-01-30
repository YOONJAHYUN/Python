import sys
input = sys.stdin.readline

def check():
    answer = 0

    my_max = max(data)
    temp = data[::-1].index(my_max)
    my_max_idx = abs(n - temp - 1)
    # print("@@@@")
    # print(temp, my_max_idx)

    for now in range(n):

        if now < my_max_idx:
            answer += my_max - data[now]

        elif now + 1 < n:
            my_max = max(data[now+1:])
            my_max_idx = data[now+1:].index(my_max) + now + 1

    return answer


t = int(input())

for _ in range(t):

    n = int(input())

    data = list(map(int, input().split()))

    print(check())
