def solution(places):
    answer = [1, 1, 1, 1, 1]
    
    '''
    p를 수집한다. 그리고 델타탐색해서 다음 p가 있는지 살핀다.
    만약 p가 있다면, 그 사이에 x가 있는지 확인
    만약 p가 없다면 다음 p 조사
    '''
    dx = [1, -1, 0, 0, 1, -1, 1, -1, 2, -2, 0, 0]
    dy = [0, 0, 1, -1, 1, -1, -1, 1, 0, 0, -2, 2]
    for l in range(5):
        lst = places[l]
        # print(lst)
        people = []
        flag = False
        for i in range(5):
            for j in range(5):
                if lst[i][j] == 'P':
                    people.append((i,j))
        # print(people)
        while people:
            
            y, x = people.pop()
            
            for k in range(12):
                ny = y + dy[k]
                nx = x + dx[k]
                
                # 범위 안에 들면 체크
                if 0 <= nx < 5 and 0 <= ny < 5 and lst[ny][nx] == 'P':
                    # 사람과 사람 사이의 파티션 유무 체크
                    sy = (ny+y) / 2
                    sx = (nx+x) / 2
                        
                    if int(sy) == sy and int(sx) == sx and lst[int(sy)][int(sx)] == "X":
                        continue
                    elif int(sy) != sy and int(sx) != sx and (lst[ny][x]=="X" and lst[y][nx]=="X"):
                        continue
                        
                        
                    else:
                        answer[l] = 0
                        flag = True

                        break
            if flag == True:
                break
                
        
    return answer