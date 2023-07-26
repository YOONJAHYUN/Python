from itertools import zip_longest as zip

def tolist(l):
    n=[]
    for i,d in enumerate(l):
        for _ in range(d):
            n.append(i+1)
    return n

def solution(cap, n, deliveries, pickups):
    d=tolist(deliveries)
    p=tolist(pickups)
    d.reverse()
    p.reverse()
    d=d[::cap]
    p=p[::cap]
    ans = 2*sum([max(x,y) for x,y in zip(d,p,fillvalue=0)])
    print(ans)
    return
solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
# solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])