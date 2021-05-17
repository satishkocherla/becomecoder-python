n,r1,r2=map(int,input().split())
for i in range(1,r2+1):
    if((n*i)%r1!=0):
        print(n,"X",i,"=",n*i)
