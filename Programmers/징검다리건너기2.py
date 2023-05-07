# 매개변수 탐색

def solution(stones, k):
    start = 0
    end = 200000000

    while start <= end:

        mid = (start + end) // 2

        count = 0
        for stone in stones:
            # 건너갈 수 있음 초기화
            if stone - mid > 0:
                count = 0
            # 건너 갈 수 없음
            else:
                count += 1
                # k개 넘을 경우 break
                if count >= k:
                    break

        # count 가 k보다 클 경우
        if count >= k:
            # mid를 줄여야됨
            end = mid - 1
        else:
            start = mid + 1
    # 왜 end가 아닌 start일까...
    # 매개변수 너무 어려웡.... ㅜㅜ.... 훈석오빠한테 물어봐야지!!!!!!!!!!
    # 언제 start를 해야하고 언제 end를 해야하는지 ..!!!
    return start


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3)