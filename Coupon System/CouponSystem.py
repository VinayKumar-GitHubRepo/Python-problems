def Level(A,lev):
    level=[]
    l=[]
    for i in A:
        if i[1]==lev:
            level.append(i)
    level.sort(key=lambda x: x[2])
    level.reverse()
    d=level[0][2]
    for i in level:
        if i[2]==d:
            l.append(i[0])
    return str(d)+"  "+str(min(l)) 
 
t=int(input())
for i in range(t):
    a=[]
    n = int(input())
    for j in range(n):
        l=input()
        x=list(map(int,l.split(' ')))
        a.append(x)
    print(Level(a,1))
    print(Level(a,2))
    print(Level(a,3)) 