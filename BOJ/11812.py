import sys
input = sys.stdin.readline

def parent(n):

    if n % K == 1 or n % K== 0:
        return n//K
    else:
        return n//K + 1


N, K, Q = map(int, input().split())

# print(parent(1))
if K == 1:
    for _ in range(Q):
        u, v = map(int, input().split())
        print(abs(u-v))
else:
    for _ in range(Q):
        u, v = map(int, input().split())
        # check(u, v)
        cnt = 0
        while True:
            if u == v:
                print(cnt)
                break
            if u > v:
                u = parent(u)
            else:
                v = parent(v)
            cnt += 1

'''
98765432111 1 2
1 98765432111
98765432111 1
'''