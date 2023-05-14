def solution(brown, yellow):
    answer = []
    
    res = brown + yellow
    
    candi = []
    for i in range(1, res):
        if int(res/i) == res/i and i >= res/i:
            candi.append((i, int(res/i)))
    # print(candi)
    
    for x, y in candi:
        if (x-2)*(y-2) == yellow:
            answer = [x, y]
            break
    
    return answer