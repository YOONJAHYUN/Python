import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    text = input().rstrip()

    n = len(text)
    cnt = 0
    left, right = 0, n-1

    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1

        else:
            # 양쪽 땡겨도 같은 경우 (abbab)
            if text[left+1] == text[right] and text[left] == text[right-1]:
                lleft = left+1
                rright = right
                flag = True

                # 왼쪽삭제 후 회문인지 검사
                while lleft < rright:
                    # 계속 같으면 진행
                    if text[lleft+1] == text[rright-1]:
                        lleft += 1
                        rright -= 1
                    else:
                        flag = False
                        break

                lleft = left
                rright = right - 1

                # 오른쪽 삭제 후 회문인지 검사
                if not flag:
                    flag = True

                    while lleft < rright:
                        if text[lleft+1] == text[rright-1]:
                            lleft += 1
                            rright -= 1
                        else:
                            flag = False
                            break

                if flag:
                    cnt += 1
                    break
                else:
                    cnt = 2
                    break
                break

            elif text[left+1] == text[right]:
                cnt += 1
                left += 2
                right -= 1
            elif text[left] == text[right-1]:
                cnt += 1
                left += 1
                right -= 2
            else:
                cnt = 2
                break

            if cnt >= 2:
                break

    if cnt == 0:
        print(0)
    elif cnt == 1:
        print(1)
    else:
        print(2)

