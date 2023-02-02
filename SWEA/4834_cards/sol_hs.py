# 훈석오빠 코드
import sys
sys.stdin = open('4834_input.txt')
input = sys.stdin.readline
#  테스트 케이스 횟수 입력
T = int(input())
# 테스트 케이스 횟수만큼 반복
for tc in range(T):
    # 카드 장수 N입력
    N = int(input())
    # 숫자 입력
    num = str(input().rstrip())
    # 숫자가 나올떄마나 횟수를 세어줄 count_num변수 생성
    count_num = [0]*10
    # num의 첫글자씩 받아와서 반복
    for i in num:
        # i는 str이기에 int로 값변환하여 인덱스 사용
        count_num[int(i)] += 1
    # count횟수를 세어줄 변수 max
    max = 0
    # 뒤에서 부터 시작
    # 클 경우 저장시킬꺼기 때문에 뒤에서 부터해서 저장
    # 앞에서부터 하면 뒤에 숫자가 더커도 횟수가 같으면 저장이 되지않음

    # 인덱스 접근하는것 중요!!! 
    # i 값을 index로 정의
    for i in range(9, -1, -1):
        if count_num[i] > max:
            max = count_num[i]
            max_index = i
    # 출력
    print(f'#{tc} {max_index} {max}')