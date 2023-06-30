def solution(board, r, c):
    answer = 0
    '''
    방향키와 엔터키를 누르는 동작 각각 1
    컨트롤 키와 방향키 1

    키 조작 횟수의 최솟값을 return
    -> 완전 탐색 + 백트래킹
    -> 제일 먼저 짝맞추는걸 목표로 한다.
    -> 커서에 닿은 거 부터 찾고, 상하좌우로 돌리기..?

    대충 풀면 안된다..
    백트래킹 형식으로 푸는게 맞는 거 같음.
    짝끼리 리스트에 담았으니, 짝에서 하나씩 빼오는 방식으로 해야할듯?

    1번 리스트에서부터 시작.. rc까지 거리구하고.. 
    2번 리스트.. rc
    ...
    6번 리스트까지 한다.

    1번리스트에서 출발했으면.. 그담것도..visited써서 해보자...

    '''

    # 짝끼리 리스트로 담는다.
    check_list = [[] for _ in range(7)]
    total = 0

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num:
                check_list[num].append((i, j))
                total += 1

    # 커서의 시작 점에 카드가 없을 수도 있으니, 델타탐색..으로..
    # 가장 가까운것에 있는 카드를 선택하게 한다.

    def choose_card(y, x):
        mul = 1
        cnt = 0
        # 상하좌우로 갈 수 있는 곳 부터 먼저 가고, 안된다면 대각선방향으로 움직여야됨
        while mul <= 5:
            for dy, dx in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy * mul, x + dx * mul

                if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx]:
                    if (dy, dx) == (0, 0):
                        cnt = 0
                    else:
                        cnt = 1
                    return (cnt, ny, nx)
            mul += 1

        # 상하좌우로 없다면, 대각선 방향으로 가자
        mul = 1
        while mul <= 5:
            for dy, dx in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
                ny, nx = y + dy * mul, x + dx * mul

                if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx]:
                    return (2, ny, nx)
            mul += 1

    # y, x = choose_card(r, c)
    # print(y, x)

    # 카드를 선택해서 뒤집고, 카운트를 세는 함수
    def check_card(y, x):
        num = board[y][x]
        one, two = check_list[num]
        cnt = 4
        sy, sx = 0, 0

        if one == (y, x):
            sy, sx = two
        else:
            sy, sx = one

        if sy == y or sx == x:
            cnt = 3
        else:
            cnt = 4

        board[sy][sx] = 0
        board[y][x] = 0
        # 새 시작점
        return (cnt, sy, sx)

    # mycnt, sy, sx = check_card(y, x)
    # print(mycnt, sy, sx)

    cnt, y, x = choose_card(r, c)
    answer += cnt
    # print(cnt)
    while total > 0:
        total -= 2
        mycnt, sy, sx = check_card(y, x)
        answer += mycnt
        # print(mycnt)

        if total == 0:
            break
        ncnt, y, x = choose_card(sy, sx)
        answer += ncnt
        # print(ncnt)
    return answer

print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))def solution(board, r, c):
    answer = 0
    '''
    방향키와 엔터키를 누르는 동작 각각 1
    컨트롤 키와 방향키 1

    키 조작 횟수의 최솟값을 return
    -> 완전 탐색 + 백트래킹
    -> 제일 먼저 짝맞추는걸 목표로 한다.
    -> 커서에 닿은 거 부터 찾고, 상하좌우로 돌리기..?

    대충 풀면 안된다..
    백트래킹 형식으로 푸는게 맞는 거 같음.
    짝끼리 리스트에 담았으니, 짝에서 하나씩 빼오는 방식으로 해야할듯?

    1번 리스트에서부터 시작.. rc까지 거리구하고.. 
    2번 리스트.. rc
    ...
    6번 리스트까지 한다.

    1번리스트에서 출발했으면.. 그담것도..visited써서 해보자...

    '''

    # 짝끼리 리스트로 담는다.
    check_list = [[] for _ in range(7)]
    total = 0

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num:
                check_list[num].append((i, j))
                total += 1

    # 커서의 시작 점에 카드가 없을 수도 있으니, 델타탐색..으로..
    # 가장 가까운것에 있는 카드를 선택하게 한다.

    def choose_card(y, x):
        mul = 1
        cnt = 0
        # 상하좌우로 갈 수 있는 곳 부터 먼저 가고, 안된다면 대각선방향으로 움직여야됨
        while mul <= 5:
            for dy, dx in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy * mul, x + dx * mul

                if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx]:
                    if (dy, dx) == (0, 0):
                        cnt = 0
                    else:
                        cnt = 1
                    return (cnt, ny, nx)
            mul += 1

        # 상하좌우로 없다면, 대각선 방향으로 가자
        mul = 1
        while mul <= 5:
            for dy, dx in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
                ny, nx = y + dy * mul, x + dx * mul

                if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx]:
                    return (2, ny, nx)
            mul += 1

    # y, x = choose_card(r, c)
    # print(y, x)

    # 카드를 선택해서 뒤집고, 카운트를 세는 함수
    def check_card(y, x):
        num = board[y][x]
        one, two = check_list[num]
        cnt = 4
        sy, sx = 0, 0

        if one == (y, x):
            sy, sx = two
        else:
            sy, sx = one

        if sy == y or sx == x:
            cnt = 3
        else:
            cnt = 4

        board[sy][sx] = 0
        board[y][x] = 0
        # 새 시작점
        return (cnt, sy, sx)

    # mycnt, sy, sx = check_card(y, x)
    # print(mycnt, sy, sx)

    cnt, y, x = choose_card(r, c)
    answer += cnt
    # print(cnt)
    while total > 0:
        total -= 2
        mycnt, sy, sx = check_card(y, x)
        answer += mycnt
        # print(mycnt)

        if total == 0:
            break
        ncnt, y, x = choose_card(sy, sx)
        answer += ncnt
        # print(ncnt)
    return answer

print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))