def solution(s):
    answer = len(s)
    '''
    변수 지정해서 압축 개수를 정한다.
    공약수인경우는 그냥 하면됨
    공약수가 아니면...?
    마지막에 한꺼번에 걍 더해줘야됨
    '''

    l = 1
    while l < len(s):
        ans = ''
        i = 0
        tmp = ''
        cnt = 1

        while True:

            # 종료조건
            if i + l > len(s):
                if cnt > 1:
                    ans += str(cnt)
                ans += tmp
                ans += s[i:]
                break
            # 앞에랑 같을 뗴
            if tmp == s[i:i + l]:
                cnt += 1
            # 앞과 같지 않을 때
            else:
                if cnt > 1:
                    ans += str(cnt)
                ans += tmp
                tmp = s[i:i + l]
                cnt = 1

            i += l

        answer = min(answer, len(ans))
        l += 1

    return answer