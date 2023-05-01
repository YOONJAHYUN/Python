import sys
input = sys.stdin.readline

def check():

    m = len(words)

    for i in range(m-1):
        if words[i] == words[i+1][0:len(words[i])]:
            print('NO')
            return
    print('YES')
    return


t = int(input())

for _ in range(t):
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    words.sort()
    check()
