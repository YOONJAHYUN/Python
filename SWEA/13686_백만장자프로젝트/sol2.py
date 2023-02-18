import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    data = list(map(int, input().split()))
    # 최댓값 저장, 최댓값 인덱스 저장
    my_max = max(data)
    max_index = data.index(my_max)
    result = 0

    for i in range(N):
        # 최댓값 인덱스보다 작고, 데이터도 작으면 결과에 더하기
        if i < max_index and data[i] < my_max:
            result += (my_max - data[i])
        # for문 돌다가 index가 같아지면 index값과 최댓값 변경해주기
        elif i == max_index:
            if i != N-1:
                my_max = max(data[i+1:N])
                # 같은 값이 있으면 인덱스 변경이 안됨..
                # 8128 이면 index 3으로 바꿔야하는데..
                max_index = (data[i+1:N].index(my_max) + i+1)
            else:
                break
    print(f'#{tc}', result)