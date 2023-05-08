def solution(stones, k):
    answer = 0

    '''
    조건
    숫자 한번밟으면 -1
    0 이되면 밟을 수 없고 그 다음으로 jump 가능
    한 명이 건넌 후 건널 수 있음
    '''

    # for 문돌리면서 하나씩 줄여준다.

    # 바깥에 while문 하고. 만약 for문에서 0이 나온다면? count를 세고 그 count 가 K 넘는 즉시 중단.
    flag = True

    while flag:
        count = 0
        for i in range(len(stones)):
            if stones[i] >= 1:
                stones[i] -= 1
                count = 0
            else:
                # 연속 체크
                count += 1
                if count >= k:
                    flag = False
                    break

        answer += 1
        # print(answer, stones)

    return answer - 1
solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3)