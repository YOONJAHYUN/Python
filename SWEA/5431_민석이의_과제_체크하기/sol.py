import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 수강생의 수 N
    # 과제를 제출한 사람의 수 K
    N, K = map(int, input().split())
    done_stduents = list(map(int, input().split()))
    studnets = list(range(1, N+1))
    for student in done_stduents:
        if student in studnets:
            idx = studnets.index(student)
            studnets.pop(idx)
    print(f'#{tc}', *studnets)




