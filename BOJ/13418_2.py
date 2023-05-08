import sys
input=sys.stdin.readline

def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])
    return disjoint[x]

N,M=map(int,input().split())

edge=[]
for i in range(M+1): # 간선은 M+1 개 입력받는다.

    A,B,C=map(int,input().split())

    edge.append((C,B,A))

edge.sort(key=lambda x:x[0])
disjoint=[ _ for _ in range(N+1) ] ; Zero=0 ; One=0 ; check_Zero=0 ; check_One=0

for value,x,y in edge:

    x=Find(x)
    y=Find(y)

    if x!=y:
        if x>y:
            disjoint[x]=y
        else:
            disjoint[y]=x
        if value==0:
            check_Zero+=1


edge.sort(key=lambda x:-x[0])
disjoint=[ _ for _ in range(N+1) ]

for value,x,y in edge:

    x=Find(x)
    y=Find(y)

    if x!=y:
        if x>y:
            disjoint[x]=y
        else:
            disjoint[y]=x
        if value==0:
            check_One+=1

print(check_Zero**2- check_One**2)