n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()

def comb(res,i,depth):
    if depth == m:
        print(*res)
        return
    if i == n:
        return

    # arr[i] 를 포함
    comb(res+[arr[i]], i +1, depth+1)

    # arr[i] 를 포함 X
    comb(res, i + 1, depth)


comb([],0,0)