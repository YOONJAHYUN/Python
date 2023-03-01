import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    # N명의 사람들에게 M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
    N, M, K = map(int, input().split())

    arrive = list(map(int, input().split()))

    # 사람수
    people = [0] * 11112

    for i in range(N):
        people[arrive[i]] += 1


    how_many_people = [0] * 11112
    how_many_people[0] = people[0]
    for i in range(1, 11112):
        how_many_people[i] = how_many_people[i-1] + people[i]

    # 진기가 만드는 붕어빵
    boong = [0] * 11112
    # idx = 1
    for i in range(M, 11112, M):
        boong[i] = K

    for i in range(1, 11112):
        boong[i] = boong[i] + boong[i-1]
    
    for i in range(11112):
        if boong[i] < how_many_people[i]:
            print(f'#{tc}', 'Impossible')
            break
    else:
        print(f'#{tc}', 'Possible')