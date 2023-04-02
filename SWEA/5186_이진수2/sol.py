import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    n = input()

    '''
    -1 승 0.5 -> 1/2
    -2 승 0.25 ->  1/4
    -3 승 0.125 -> 1/8
    -4 승       -> 1/16
    
    '''

    print(n)

    for i in range(2, len(n)-1):

