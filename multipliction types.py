n,r1,r2=map(int,input().split())
inc=1
if(r1>r2):
    inc=-1
for i in range(r1,r2+inc,inc):
    print(n,"X",i,"=",n*i)
