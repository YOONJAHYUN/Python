import sys
input = sys.stdin.readline

n, l = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]


'''
경사로 설치 조건
1. 경사로는 낮은 칸에 놓으며 l개의 연속된 칸에 경사로의 바닥이 모두 접해야 함
2. 낮은 칸과 높은 칸의 높이 차이는 1
3. 경사로를 높을 낮은 칸의 높이는 모두 같아야함. l개 연속

'''

def function1(data):
    global ans

    for i in range(n):
        if len(set(data[i])) == 1:
            ans += 1
        else:
            ans += check(data[i])
            print(ans,data[i])

def check(lst):
    '''
    set해서 길이가 1이면 경사로를 놓을 수 있음
    놓고나서 0번째는 -1과 같아야하고,=> +- 1차이,  l번째는  l+1과 같아야함 동일
    '''

    i = 0

    while i+l < n:

        now = lst[i:i+l]

        if len(set(now)) == 1:
            # 경사로를 놓을 수 있음
            if (i-1 >= 0) and (i+l < n) and ((lst[i] == lst[i-1] and (abs(lst[i+l-1] - lst[i+l]) == 1)) or ((lst[i+l] == lst[i+l-1] and (abs(lst[i] - lst[i-1]) == 1)))):
                i += l
            else:
                i += 1
        # else:
        #     return False

    return True


ans = 0

function1(data)
data = list(map(list, zip(*data)))
function1(data)

print(ans)
