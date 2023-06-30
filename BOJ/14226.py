import sys
from collections import deque
input = sys.stdin.readline

def BFS(num):

    q = deque()
    # 현재갯수, 시간, 복사된갯수
    # 시작할때 복사한 상태라고 가정하기
    q.append((1, 1, 1))
    v = [[] for _ in range(num+1)]
    while q:
        now, time, copy = q.popleft()
        v.append((now, time, copy))
        # print(now, time, copy)
        if now == num:
            print(time)
            return

        # 방문체크
        if (now+copy, copy) not in v[time+1]:
            # 복사되어있는 거 그대로 붙여넣기
            if now+copy <= num:
                q.append((now+copy, time+1, copy))
                v[time+1].append((now+copy, copy))

        if (now, now) not in v[time+1]:
            # 새로 복사
            q.append((now, time+1, now))
            v[time + 1].append((now, now))


        if (now-1, copy) not in v[time+1]:
            # 삭제하기
            if now > 1:
                q.append((now-1, time+1, copy))
                v[time + 1].append((now-1, copy))


'''
1 개 이미 있음

1. 저장
2. 붙여넣기
3. 삭제
'''
s = int(input())
BFS(s)