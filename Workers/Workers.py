n=int(input())
K=list(map(int,input().split()))
V=list(map(int,input().split()))
min_1,min_2,min_3=99999,99999,99999
for i in range(n):
    if(V[i]==1):
        min_1=min(min_1,K[i])
    elif(V[i]==2):
        min_2=min(min_2,K[i])
    else:
        min_3=min(min_3,K[i])
if((min_1+min_2)<min_3):
    print(min_1+min_2)
else:
    print(min_3)
 