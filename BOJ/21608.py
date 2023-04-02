import sys
from collections import Counter
input = sys.stdin.readline

'''
1 좋아하는 학생이 인접한 자리
2 비어있는 칸이 가장 많은 자리
3 행의 번호가 가장 작은 칸
4 열의 번호가 가장 작은 칸
'''


N = int(input())
arr = [[0]*N for _ in range(N)]
students = [[0] for _ in range(N**2+1)]
dy = [0,0,-1,1]
dx = [1,-1,0,0]

for i in range(N**2):
    stu, *fav = map(int, input().split())
    students[stu] = fav

    # 첫 학생은 항상 (1,1) 가운데에 위치함.
    if i == 0:
        arr[1][1] = stu
    # 마지막 학생은 남은자리
    elif i == N**2 -1:
        for j in range(N):
            for k in range(N):
                if arr[j][k] == 0:
                    arr[j][k] = stu
                    break

    # 두번째 학생 부터
    else:
        # 좋아하는 학생이 자리에 앉아 있는지 찾는다.
        my_fav = []
        for j in range(N):
            for k in range(N):
                if arr[j][k] in fav:
                   my_fav.append([j,k])
        # 좋아하는 학생이 있다면,
        # 좋아하는 학생이 근접한 곳으로 간다.
        # dy = [0,0,-1,1]
        # dx = [1,-1,0,0]
        seat = []
        # 좋아하는 학생들 자리에서 옆자리가 얼마나 비었는지 체크한다.
        for sy, sx in my_fav:
            for k in range(4):
                ny = sy + dy[k]
                nx = sx + dx[k]
                if 0 <= nx < N and 0 <= ny < N:
                    # 그 친구 옆이 비어있다면 seat에 넣는다.
                    if arr[ny][nx] == 0:
                        # 넣을때 그 seat 옆에 빈자리도 같이 넣어준다.
                        cnt = 0
                        for l in range(4):
                            nny = ny + dy[l]
                            nnx = nx + dx[l]

                            if 0 <= nnx < N and 0 <= nny < N and arr[nny][nnx]==0:
                                cnt += 1

                        seat.append((ny, nx, cnt))

                        # seat에 자리를 넣는다.
                        # if seat[ny, nx]:
                        #     seat[ny, nx] += 1
                        # else:
                        #     seat[ny,nx] = 1

        # seat가 안만들어지는경우에 인덱스에러가 생김
        # seat의 후보들이 정해졌을 때
        if seat:
            # seat돌고 나서 가장 빈도가 높은 자리를 고르기 위해 정렬한다.
            # 빈자리가 많고, x, y 순으로 정렬
            seat.sort(key=lambda x: (-x[2], x[0], x[1]))
            # seat내에서 가장 빈도가 높게 나온애를 뽑는다.
            my_seat = Counter(seat).most_common(1)
            # print(Counter(seat).most_common(1))
            seat_y, seat_x = my_seat[0][0][0], my_seat[0][0][1]
            # print(seat_x, seat_y)
            # 자리에 앉히기
            arr[seat_y][seat_x] = stu
        # seat가 없다면, 비어있는 자리 중에서 가장 빈자리가 많은 곳으로 배치됨
        else:

            max_seat = []
            max_count = -1
            for ii in range(N):
                for jj in range(N):

                    if arr[ii][jj] == 0:
                        seat_count = 0
                        # 근처에 빈자리 count
                        # dy = [0, 0, -1, 1]
                        # dx = [1, -1, 0, 0]
                        for kk in range(4):
                            my = ii + dy[kk]
                            mx = jj + dx[kk]
                            if 0<= my < N and 0 <= mx < N and arr[my][mx] == 0:
                                seat_count += 1
                        if seat_count > max_count:
                            max_count = seat_count
                            max_seat = [ii,jj]

            seat_y, seat_x = max_seat[0], max_seat[1]
            # print(seat_x, seat_y)
            # 자리에 앉히기
            arr[seat_y][seat_x] = stu

# for i in arr:
#     print(i)
result = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        stu = arr[i][j]
        # 학생들 주위에 좋아하는 사람 카운트 세기
        # dy = [0, 0, -1, 1]
        # dx = [1, -1, 0, 0]
        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in students[stu]:
                    cnt += 1

        if cnt == 4:
            result += 1000
        elif cnt == 3:
            result += 100
        elif cnt == 2:
            result += 10
        elif cnt == 1:
            result += 1

print(result)